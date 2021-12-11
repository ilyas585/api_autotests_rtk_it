from clients.regions import ApiRegions
from clients.devices import ApiDevices


class ApiHousehold:
    def __init__(self):
        self.regions = ApiRegions()
        self.devices = ApiDevices()
