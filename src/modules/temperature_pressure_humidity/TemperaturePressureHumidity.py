#!/usr/bin/env python3
"""This class will contain methods that -
1. Use the BME-280 sensor to measure indoor pressure & humidity levels at 5 second intervals
2. Use the BME-280 sensor to measure the ambient temperature at 5 second intervals simultaneously with a TMP-36 sensor
"""

from . import BME280
from ..gas_pollution import ADS1015
import RPi.GPIO as GPIO

from src.modules import CPU_TEMPERATURE_FILE, TMP_36, MICS6814_HEATER_PIN
from src.modules.temperature_pressure_humidity.TemperaturePressureHumidityModel import TemperaturePressureHumidityModel


# def setup():
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(MICS6814_HEATER_PIN, GPIO.OUT)
#     GPIO.output(MICS6814_HEATER_PIN, 1)
#
#
# def cleanup():
#     GPIO.output(MICS6814_HEATER_PIN, 0)


def get_cpu_temperature():
    """
    Get the CPU temperature. While it won't be directly used for temperature compensation, it is going to be used to derive
    the compensation factor for achieving accurate temperatures from the TMP36 or the BME280 sensors.
    :return:
    """
    cpu_temp = -69.420
    try:
        with open(CPU_TEMPERATURE_FILE, "r") as cpu_temp_file:
            cpu_temp = int(cpu_temp_file.read()) / 1000
            cpu_temp_file.close()
    except FileNotFoundError as ff:
        print('File Not Found with Error: {}'.format(ff))

    return cpu_temp


class TemperaturePressureHumidity:
    def __init__(self):
        # init the BME-280 sensor
        self.bme280 = BME280()
        self.bme280.setup('forced')

        # init the ads1115 chip to control TMP-36 sensor
        self.ads1015 = ADS1015(i2c_addr=0x49)
        self.ads1015.set_mode('single')
        self.ads1015.set_programmable_gain(2.048)
        self.ads1015.set_sample_rate(128)

        # init the model class
        self.environment = TemperaturePressureHumidityModel()

    def populate_sensor_data(self):
        """
        Driver Method compiling the Environment factors' measurement values
        :return:
        """
        t1, p1, h1 = self.measure_bme280_values()
        self.environment.bme_temperature = t1
        self.environment.raw_pressure = p1
        self.environment.raw_humidity = h1

        tmp1 = self.measure_tmp36_values(TMP_36)
        self.environment.tmp_temperature = tmp1

        self.environment.cpu_temperature = get_cpu_temperature()

        return self.environment

    def measure_bme280_values(self):
        return self.bme280.update_sensor()

    def measure_tmp36_values(self, channel_name) -> float:
        # setup()
        voltage = self.ads1015.get_voltage(channel_name)
        tmp_36 = 100 * (voltage - 0.5)
        # cleanup()
        return tmp_36
