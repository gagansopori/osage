#!/usr/bin/env python3

from src.models.LightProximityModel import LightProximityModel
from library.drivers import LTR559


class LightProximity:
    def __init__(self):
        # initialize sensor
        self.ltr559 = LTR559()
        # initialize model class
        self.light = LightProximityModel()

    def measure_ltr559_values(self):
        self.light.lux = self.ltr559.get_lux()
        self.light.proximity = self.ltr559.get_proximity()
        return self.light
