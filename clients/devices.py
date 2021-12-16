import copy
from config import Config
from helpers.helper import ApiHelper


class ApiDevices:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        self.helper = ApiHelper()

    def open_device_by_id(self, token, device_id, relay, delay):
        api_method = f"/api/v4/devices/{device_id}/open"
        url = self.url + api_method
        resp_dict = {
            "relay": relay,
            "delay": delay
        }

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = self.helper.request("POST", url, headers=headers, json=resp_dict)
        return response
