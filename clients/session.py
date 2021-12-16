from config import Config
from helpers.helper import ApiHelper
import copy


class ApiSessions:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}
        self.helper = ApiHelper()

    def post_login(self, email, password):
        api_method = "/internal/api/v3/login"
        url = self.url + api_method

        req_dict = {
            "email": email,
            "password": password
        }

        headers = copy.deepcopy(self.default_headers)
        headers["Content-Type"] = "application/json"

        response = self.helper.request("POST", url, headers=headers, json=req_dict)
        return response
