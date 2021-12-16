from clients.api_helper import ApiHousehold
from checkers.checkers_helper import Checkers
from config import Config


class Application:
    def __init__(self):
        self.configs = Config()
        self.api = ApiHousehold()
        self.checkers = Checkers()
        self.token_admin = self.try_login(self.configs.admin_email, self.configs.admin_password)
        self.token_admin = self.configs.token if "unsuccessful login" in self.token_admin else self.token_admin
        self.ids = 90

    def try_login(self, email, password):
        try:
            response = self.api.session.post_login(email, password)
            return response.json()["data"]["key"]["access_token"]
        except:
            return f"unsuccessful login as {email}"
