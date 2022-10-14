#!/usr/bin/env python3

from . import LTR559
from .LightProximityModel import LightProximityModel


class LightProximity:
    def __init__(self):
        self.ltr559 = LTR559()
        self.light = LightProximityModel()

    def measure_ltr559_values(self):
        self.light.lux = self.ltr559.get_lux()
        self.light.proximity = self.ltr559.get_proximity()
        return self.light
