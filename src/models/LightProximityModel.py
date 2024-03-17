
class LightProximityModel:
    def __init__(self):
        self._lux: float = 0.0
        self._proximity: float = 0.0

    @property
    def lux(self):
        return self._lux

    @lux.setter
    def lux(self, ilx):
        self._lux = ilx

    @property
    def proximity(self):
        return self._proximity

    @proximity.setter
    def proximity(self, prox):
        self._proximity = prox
    