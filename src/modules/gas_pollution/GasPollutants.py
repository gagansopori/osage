import math

import RPi.GPIO as GPIO

from src.modules import OXIDIZING_GASES, REDUCING_GASES, NH3_AMMONIA
from src.modules.gas_pollution import ADS1015
from src.modules.gas_pollution.GasPollutionModel import GasPollutionModel

MICS6814_HEATER_PIN = 24


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MICS6814_HEATER_PIN, GPIO.OUT)
    GPIO.output(MICS6814_HEATER_PIN, 1)


def cleanup():
    GPIO.output(MICS6814_HEATER_PIN, 0)


class GasPollutants:
    def __init__(self):
        # init the ADS-1015 sensor
        self.ads_1015 = ADS1015(i2c_addr=0x49)
        self.ads_1015.set_mode('single')
        self.ads_1015.set_programmable_gain(6.148)
        if self.ads_1015.detect_chip_type() == 'ADS1115':
            self.ads_1015.set_sample_rate(128)
        else:
            self.ads_1015.set_sample_rate(1600)

        self.gas = GasPollutionModel()

    def fetch_gas_ppm(self, warm_up_indicator):
        """
        Driver Method that fetches all the raw gas-sensor values (measured in Ohms) & converts them to
        parts-per-million (ppm) values for a human understandable system.
        TODO: Add logic to persist the r0 values (o_init, a_init, r_init) & calculate avg. over-time for Rs/r0 Ratio
        TODO: Rs/r0 is the same thing as current_value/init_value.
        TODO: refer to: https://github.com/roscoe81/enviro-monitor/blob/master/Northcliff_AQI_Monitor_Gen.py#L382
        :param warm_up_indicator:
        :return:
        """
        # o_init, r_init, a_init, o_current, r_current, a_current = None, None, None, None, None, None
        # if warm_up_indicator:
        #     # R0 overtime for Oxidizing Gases
        #     o_init = self.read_gas_raw(OXIDIZING_GASES)
        #     if not self.gas.oxidizing_init == 0.0:
        #         o_init = round((o_init + self.gas.oxidizing_init) / 2)
        #     self.gas.oxidizing_init = o_init
        #
        #     # R0 overtime for Reducing Gases
        #     r_init = self.read_gas_raw(REDUCING_GASES)
        #     if not self.gas.reducing_init == 0.0:
        #         r_init = round((r_init + self.gas.reducing_init) / 2)
        #     self.gas.reducing_init = r_init
        #
        #     # R0 overtime for Ammonia (NH3)
        #     a_init = self.read_gas_raw(NH3_AMMONIA)
        #     if not self.gas.nh3ammonia_init == 0.0:
        #         a_init = round((a_init + self.gas.reducing_init) / 2)
        #     self.gas.nh3ammonia_init = a_init
        # else:
        #     o_init = self.gas.oxidizing_init
        #     r_init = self.gas.reducing_init
        #     a_init = self.gas.nh3ammonia_init

        o_current = self.read_gas_raw(OXIDIZING_GASES)
        r_current = self.read_gas_raw(REDUCING_GASES)
        a_current = self.read_gas_raw(NH3_AMMONIA)
        o_init = o_current
        r_init = r_current
        a_init = a_current

        self.gas = self.raw_to_ppm(o_init, r_init, a_init, o_current, r_current, a_current)

        return self.gas

    def read_gas_raw(self, channel_name):
        setup()
        try:
            v = self.ads_1015.get_voltage(channel_name)
            print(f"{channel_name} has voltage of {v}")
            # x, Ri = self.read_gas_sensor(channel_name)
            # print(f"HWCave's - {channel_name} has voltage of {x}")
            v = (v * 56000) / (3.3 - v)
            # print(f"HW Caves reading for {channel_name} - {1.0 / ((1.0 / ((x * 56000.0) / (3.3 - x))) - (1.0 / Ri))}")
        except ZeroDivisionError:
            v = 0
        cleanup()
        return v

        # return 1.0 / ((1.0 / ((v * 56000.0) / (3.3 - v))) - (1.0 / Ri))

    # def read_gas_sensor(self, ch):
    #     self.ads_1015.set_programmable_gain(4.096)
    #     Ri = 6000000
    #     v = self.ads_1015.get_voltage(ch)
    #
    #     if v <= 1.0:
    #         self.ads_1015.set_programmable_gain(1.024)
    #         v = self.ads_1015.get_voltage(ch)
    #         Ri = 3000000
    #     elif v <= 2.0:
    #         self.ads_1015.set_programmable_gain(2.048)
    #         v = self.ads_1015.get_voltage(ch)
    #         Ri = 6000000
    #
    #     return v, Ri

    def raw_to_ppm(self, o_init, r_init, a_init, o_current, r_current, a_current):
        gas_vals = GasPollutionModel()
        print(f"{o_init}, {r_init}, {a_init}, {o_current}, {r_current}, {a_current}")

        # Oxidizing Ratio
        try:
            rsr0_oxd = o_current / o_init if o_current / o_init > 0 else 0.0001
        except ZeroDivisionError:
            rsr0_oxd = 0.0001
        # if o_init is not None and o_current / o_init > 0:
        #     rsr0_oxd = o_current / o_init
        # else:
        #     rsr0_oxd = 0.0001
        print(f"Rs/R0 Oxidizing - {rsr0_oxd}")
        gas_vals.ads_oxidizing = o_current
        gas_vals.oxidizing_ppm = math.pow(10, math.log10(rsr0_oxd) - 0.8129)

        # Reducing Ratio
        try:
            rsr0_red = r_current / r_init if r_current / r_init > 0 else 0.0001
        except ZeroDivisionError:
            rsr0_red = 0.0001
        # if r_init is not None and r_current / r_init > 0:
        #     rsr0_red = r_current / r_init
        # else:
        #     rsr0_red = 0.0001
        print(f"Rs/R0 Reducing - {rsr0_red}")
        gas_vals.ads_reducing = r_current
        gas_vals.reducing_ppm = math.pow(10, -1.25 * math.log10(rsr0_red) + 0.64)

        # Ammonia Ratio
        try:
            rsr0_nh3 = a_current / a_init if a_current / a_init > 0 else 0.0001
        except ZeroDivisionError:
            rsr0_nh3 = 0.0001
        # if a_init is not None and a_current / a_init > 0:
        #     rsr0_nh3 = a_current / a_init
        # else:
        #     rsr0_nh3 = 0.0001
        print(f"Rs/R0 Ammonia - {rsr0_nh3}")
        gas_vals.ads_nh3ammonia = a_current
        gas_vals.nh3ammonia_ppm = math.pow(10, -1.8 * math.log10(rsr0_nh3) - 0.163)

        return gas_vals
