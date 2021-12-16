import copy
from config import Config
from helpers.helper import ApiHelper


class ApiBuildings:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        self.helper = ApiHelper()

    def get_building_by_id(self, token, building_id):
        api_method = f"/api/v4/flatgramms/buildings/{building_id}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = self.helper.request("GET", url, headers=headers)
        return response
