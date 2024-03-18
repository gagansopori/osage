#!/usr/bin/env python 3
""" This class drives the following features -
1. TMP-36 temperature via an ADS-1*15 chip on the Enviro+ board
2. Get CPU temperature on a Raspberry Pi with debian linux
3. TMP-36 temperature on a board from an independent board. (Maybe...)
"""
import time

from library.drivers.ADS1X15 import ADS1015
from src.modules import CPU_TEMPERATURE_FILE


class TMP36:
    def __init__(self):
        # init the ads1115 chip to control TMP-36 sensor
        self.ads1015 = ADS1015(i2c_addr=0x49)
        self.ads1015.set_mode('single')
        self.ads1015.set_programmable_gain(4.096)
        self.ads1015.set_sample_rate(128)

    def get_tmp36_temperature(self, channel_name: str) -> float:
        """
        Method returns the temperature converted from the measured voltage on the TMP-36 analog temperature sensor.
        The temperature on the tmp-36 ranges from -40\u2103 to 125\u2103

        :param channel_name:
        :return:
        """
        voltage = self.ads1015.get_voltage(channel_name)
        print(f"Voltage = {voltage}")
        time.sleep(1)
        # Conversion formula is different for 3.3V & 5V devices
        tmp_36 = 100 * (voltage - 0.5)
        print(f"temperature - {tmp_36}")
        return tmp_36

    def get_cpu_temperature(self) -> float:
        """
        Method returns the cpu temperature if the cpu_temperature_file is present. Configuring the cpu temp file
        will be done automatically based on the OS Flavor.

        :return: float
        """
        default_cpu_temp = -69.420
        try:
            with open(CPU_TEMPERATURE_FILE, "r") as cpu_temp_file:
                return int(cpu_temp_file.read()) / 1000
        except FileNotFoundError as ff:
            print('File Not Found with Error: {}'.format(ff))

        return default_cpu_temp
