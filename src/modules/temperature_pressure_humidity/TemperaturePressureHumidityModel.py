class TemperaturePressureHumidityModel:
    def __init__(self):
        self._raw_temperature: float = 0.0
        self._cpu_temperature: float = 0.0
        self._calibrated_temperature: float = 0.0

        self._raw_pressure: float = 0.0
        self._calibrated_pressure: float = 0.0

        self._raw_humidity: float = 0.0
        self._calibrated_humidity: float = 0.0

    @property
    def raw_temperature(self):
        return self._raw_temperature

    @raw_temperature.setter
    def raw_temperature(self, fc):
        self._raw_temperature = fc

    @property
    def cpu_temperature(self):
        return self._cpu_temperature

    @cpu_temperature.setter
    def cpu_temperature(self, cpu):
        self._cpu_temperature = cpu

    @property
    def calibrated_temperature(self):
        return self._calibrated_temperature

    @calibrated_temperature.setter
    def calibrated_temperature(self, fc_fine):
        self._calibrated_temperature = fc_fine


    @property
    def raw_pressure(self):
        return self._raw_pressure

    @raw_pressure.setter
    def raw_pressure(self, hPa):
        self._raw_pressure = hPa

    @property
    def calibrated_pressure(self):
        return self._calibrated_pressure

    @calibrated_pressure.setter
    def calibrated_pressure(self, hPa_c):
        self._calibrated_pressure = hPa_c

    @property
    def raw_humidity(self):
        return self._raw_humidity

    @raw_humidity.setter
    def raw_humidity(self, hum):
        self._raw_humidity = hum

    @property
    def calibrated_humidity(self):
        return self._calibrated_humidity

    @calibrated_humidity.setter
    def calibrated_humidity(self, hum_c):
        self.calibrated_humidity = hum_c
