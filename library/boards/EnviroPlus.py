from library.boards import BoardBuilder
from library.drivers.ADS1X15 import ADS1015
from library.drivers.BME280 import BME280
from library.drivers.LTR559 import LTR559


class EnviroPlus:
    def __init__(self):
        self.build_enviro_plus(BoardBuilder())

    def build_enviro_plus(self, builder):
        return builder\
            .set_bme280_env_sensor(BME280())\
            .set_ltr559_light_sensor(LTR559())\
            .set_ads_1015_gas_sensor(ADS1015())\
            .build()