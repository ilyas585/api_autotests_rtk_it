import requests
from pprint import pprint


class ApiHelper:
    @staticmethod
    def request(method, url, headers=None, json=None, params=None):
        """
        :param method: GET, POST, PUT, DELETE
        :return:
        """
        response = requests.request(method, url, headers=headers, json=json, params=params)

        req_resp_data = f"""
        REQUEST
        url: {response.url}
        method: {response.request.method}
        headers: {response.request.headers}
        body: {response.request.body}
    
        RESPONSE
        headers: {response.headers}
        code: {response.status_code}
        body: {response.text}
        """

        pprint(req_resp_data)

        return response
