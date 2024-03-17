from library.boards import BoardBuilder
from library.drivers.BME280 import BME280
from library.drivers.LTR559 import LTR559


class EnviroMini:
    def __init__(self):
        self.build_enviro_mini(BoardBuilder())

    def build_enviro_mini(self, builder):
        return builder\
            .set_bme280_env_sensor(BME280())\
            .set_ltr559_light_sensor(LTR559())\
            .build()
