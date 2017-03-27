from .enum import DigitalOutput

from .. import models


class WaterVolume:

    def __init__(self, min_, max_):
        self.min_ = min_
        self.max_ = max_

    def pump_in(self):
        volume = models.water_volume.last()

        if volume is None:
            return DigitalOutput.any

        volume = volume.volume

        if volume >= self.max_:
            return DigitalOutput.off

        # TODO: to be removed
        if volume <= self.min_:
            return DigitalOutput.on

        return DigitalOutput.any

    def pump_out(self):
        if models.water_volume.last() <= self.min_:
            return DigitalOutput.off

        return DigitalOutput.any