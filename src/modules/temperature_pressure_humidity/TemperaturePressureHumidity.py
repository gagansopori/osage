#!/usr/bin/env python3
"""This class will contain methods that -
1. Use the BME-280 sensor to measure indoor pressure & humidity levels at 5 second intervals
2. Use the BME-280 sensor to measure the ambient temperature at 5 second intervals simultaneously with a TMP-36 sensor
"""
from . import BME280

from src.modules import CPU_TEMPERATURE_FILE
from src.modules.temperature_pressure_humidity.TemperaturePressureHumidityModel import TemperaturePressureHumidityModel


class TemperaturePressureHumidity:
    def __init__(self):
        # init the sensor
        self.bme280 = BME280()
        self.bme280.setup('forced')

        # init the model class
        self.environment = TemperaturePressureHumidityModel()

    # def measure_humidity(self):
    #     """This method collects indoor environment humidity readings from the BME280 Sensor """
    #     self.environment.raw_humidity = self.bme280.get_humidity()
    #     return self.environment
    #
    # def measure_pressure(self):
    #     """This method collects indoor environment pressure readings from the BME280 Sensor"""
    #     self.environment.raw_pressure = self.bme280.get_pressure()
    #     return self.environment
    #
    # def measure_temperature(self):
    #     """This method collects indoor environment temperature readings from the BME280 Sensor"""
    #     self.environment.raw_temperature = self.bme280.get_temperature()
    #     self.environment.cpu_temperature = self.get_cpu_temperature()
    #     return self.environment

    def get_cpu_temperature(self):
        cpu_temp = -69.420
        try:
            with open(CPU_TEMPERATURE_FILE, "r") as cpu_temp_file:
                cpu_temp = int(cpu_temp_file.read()) / 1000
                cpu_temp_file.close()
        except FileNotFoundError as fnf:
            print('File Not Found with Error: {}'.format(fnf))

        return cpu_temp

    def get_bme_values(self):
        self.environment.raw_temperature, self.environment.raw_pressure, self.environment.raw_humidity = self.bme280.update_sensor()
        self.environment.cpu_temperature = self.get_cpu_temperature()

        return self.environment
