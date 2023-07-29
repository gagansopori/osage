class TemperaturePressureHumidityModel:
    def __init__(self):
        self._bme_temperature: float = 0.0
        self._cpu_temperature: float = 0.0
        self._tmp_temperature: float = 0.0

        self._raw_pressure: float = 0.0
        self._calibrated_pressure: float = 0.0

        self._raw_humidity: float = 0.0
        self._calibrated_humidity: float = 0.0

    @property
    def bme_temperature(self):
        return self._bme_temperature

    @bme_temperature.setter
    def bme_temperature(self, fc):
        self._bme_temperature = fc

    @property
    def cpu_temperature(self):
        return self._cpu_temperature

    @cpu_temperature.setter
    def cpu_temperature(self, cpu):
        self._cpu_temperature = cpu

    @property
    def tmp_temperature(self):
        return self._tmp_temperature

    @tmp_temperature.setter
    def tmp_temperature(self, fc_fine):
        self._tmp_temperature = fc_fine

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
