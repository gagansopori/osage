class GasPollutionModel:
    def __init__(self):
        self._ads_nh3ammonia: float = 0.0
        self._nh3ammonia_ppm: float = 0.0

        self._ads_oxidizing: float = 0.0
        self._oxidizing_ppm: float = 0.0

        self._ads_reducing: float = 0.0
        self._reducing_ppm: float = 0.0

    @property
    def ads_nh3ammonia(self):
        return self._ads_nh3ammonia

    @ads_nh3ammonia.setter
    def ads_nh3ammonia(self, nh3):
        self._ads_nh3ammonia = nh3

    @property
    def nh3ammonia_ppm(self):
        return self._nh3ammonia_ppm

    @nh3ammonia_ppm.setter
    def nh3ammonia_ppm(self, nh3_ppm):
        self._nh3ammonia_ppm = nh3_ppm

    @property
    def ads_oxidizing(self):
        return self._ads_oxidizing

    @ads_oxidizing.setter
    def ads_oxidizing(self, oxd):
        self._ads_oxidizing = oxd

    @property
    def oxidizing_ppm(self):
        return self._oxidizing_ppm

    @oxidizing_ppm.setter
    def oxidizing_ppm(self, oxd_ppm):
        self._oxidizing_ppm = oxd_ppm

    @property
    def ads_reducing(self):
        return self._ads_reducing

    @ads_reducing.setter
    def ads_reducing(self, red):
        self._ads_reducing = red

    @property
    def reducing_ppm(self):
        return self._reducing_ppm

    @reducing_ppm.setter
    def reducing_ppm(self, red_ppm):
        self._reducing_ppm = red_ppm
