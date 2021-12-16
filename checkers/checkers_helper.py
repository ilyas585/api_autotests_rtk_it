from checkers.regions import CheckerRegions
from checkers.devices import CheckerDevice
from checkers.general import GeneralChecker


class Checkers:
    def __init__(self):
        self.regions = CheckerRegions()
        self.device = CheckerDevice()
        self.general = GeneralChecker()

