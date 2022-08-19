#!/usr/bin/env python3
"""This class will contain methods that -
1. Use the BME-280 sensor to measure indoor pressure & humidity levels at 5 second intervals
2. Use the BME-280 sensor to measure the ambient temperature at 5 second intervals simultaneously with a TMP-36 sensor
3.
"""
import os, time, numpy
# from bme280 import BME280

from src.modules.temp_pressure_humidity.BME280Model import TemperaturePressureHumidityModel


class TemperaturePressureHumidity:
    def __init__(self):
        # init the sensor
        self.bme280 = BME280()
        # init the model class
        self.environment = TemperaturePressureHumidityModel()

    '''This method collects readings from the BME280 Sensor for getting the humidity of the environment at 5 second 
    intervals '''
    def measure_humidity(self):
        pass

    def measure_pressure(self):
        pass

    '''This method takes temperature readings'''
    def measure_temperature(self):
        pass
