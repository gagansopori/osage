
class Board:
    def __init__(self, builder):
        self.ads_1015_gas_sensor = builder.ads_1015_gas_sensor
        self.bme280_env_sensor = builder.bme280_env_sensor
        self.ltr559_light_sensor = builder.ltr559_light_sensor


class BoardBuilder:
    def __init__(self, builder):
        self.ads_1015_gas_sensor = None
        self.bme280_env_sensor = None
        self.ltr559_light_sensor = None

    def build(self):
        return Board(self)

    def set_ads_1015_gas_sensor(self, value):
        self.ads_1015_gas_sensor = value
        return self

    def set_bme280_env_sensor(self, value):
        self.ads_1015_gas_sensor = value
        return self

    def set_ltr559_light_sensor(self, value):
        self.ads_1015_gas_sensor = value
        return self
