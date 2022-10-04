class GasPollutionModel:
    def __init__(self):
        self._ads_nh3ammonia: float = 0.0
        self._ads_oxidizing: float = 0.0
        self._ads_reducing: float = 0.0

    @property
    def ads_nh3ammonia(self):
        return self._ads_nh3ammonia

    @ads_nh3ammonia.setter
    def ads_nh3ammonia(self, nh3):
        self._ads_nh3ammonia = nh3

    @property
    def ads_oxidizing(self):
        return self._ads_oxidizing

    @ads_oxidizing.setter
    def ads_oxidizing(self, oxd):
        self._ads_oxidizing = oxd

    @property
    def ads_reducing(self):
        return self._ads_reducing

    @ads_reducing.setter
    def ads_reducing(self, red):
        self._ads_reducing = red
