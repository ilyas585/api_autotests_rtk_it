import copy
from config import Config
from helpers.helper import ApiHelper


class ApiRegions:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        self.helper = ApiHelper()

    def get_configs_regions(self, token):
        api_method = "/api/v4/configs/regions"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = self.helper.request("GET", url, headers=headers)
        return response
