from clients.regions import ApiRegions
from clients.devices import ApiDevices
from clients.session import ApiSessions
from clients.buildings import ApiBuildings


class ApiHousehold:
    def __init__(self):
        self.regions = ApiRegions()
        self.devices = ApiDevices()
        self.session = ApiSessions()
        self.buildings = ApiBuildings()
