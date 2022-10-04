import atexit
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
    # atexit.register(cleanup)

def cleanup():
    GPIO.output(MICS6814_HEATER_PIN, 0)


class GasPollutants:
    def __init__(self):
        # init the ADS-1015 sensor
        self.ads_1015 = ADS1015(i2c_addr=0x49)
        self.ads_1015.set_mode('single')
        self.ads_1015.set_programmable_gain(6.148)
        self.ads_1015.set_sample_rate(128)

        # init the GPIO for MICS-6814 sensor
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(MICS6814_HEATER_PIN, GPIO.OUT)
        # GPIO.output(MICS6814_HEATER_PIN, 1)

        self.gas = GasPollutionModel()

    def measure_ads1015_values(self):
        self.gas.ads_oxidizing = self.measure_gas_values(OXIDIZING_GASES)
        self.gas.ads_reducing = self.measure_gas_values(REDUCING_GASES)
        self.gas.ads_nh3ammonia = self.measure_gas_values(NH3_AMMONIA)

        return self.gas

    def measure_gas_values(self, channel_name):
        setup()
        try:
            v = self.ads_1015.get_voltage(channel_name)
            print(v)
            v = (v * 56000) / (3.3 - v)
        except ZeroDivisionError:
            v = 0
        cleanup()
        return v
        # v, Ri = self.read_gas_sensor(channel)
        # return 1.0 / ((1.0 / ((v * 56000.0) / (3.3 - v))) - (1.0 / Ri))

    # def read_gas_sensor(self, ch):
    #     channel_name = 'in' + chr(48 + ch) + '/gnd'
    #     self.ads_1015.set_programmable_gain(4.096)
    #     Ri = 6000000
    #     v = self.ads_1015.get_voltage(channel_name)
    #
    #     if v <= 1.0:
    #         self.ads_1015.set_programmable_gain(1.024)
    #         v = self.ads_1015.get_voltage(channel_name)
    #         Ri = 3000000
    #     elif v <= 2.0:
    #         self.ads_1015.set_programmable_gain(2.048)
    #         v = self.ads_1015.get_voltage(channel_name)
    #         Ri = 6000000
    #
    #     return v, Ri
