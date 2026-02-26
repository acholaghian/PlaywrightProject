import json
import os

class Config():

    def __init__(self, env):
        self.env = env
        self.config_data = self._load_env_json()


    def _load_env_json(self):
        env_path = os.path.join(os.path.dirname(__file__), "env.json")
        with open(env_path, "r") as file:
            data =json.load(file)
        return data[self.env]

    # Getting the base URL for the website from the JSON file, or from TEST_ENV as fallback
    @property
    def base_url(self):
        return self.config_data["base_url"]
        if not base_url:
            return os.getenv("TEST_BASEURL") # If no data from env.json, fallback to TEST_ENV paramter
            if not base_url:
                raise ValueError("BASE URL not set in environment file nor provided as TEST_ENV parameter")
    
    # Supply the credential by running TEST_USERNAME=<youruser>
    @property
    def username(self):
        return self.config_data["username"]
        if not username:
            return os.getenv("TEST_USERNAME") # If no data from env.json, fallback to TEST_ENV parameter
            if not username:
                raise ValueError("USERNAME not set in environment file nor provided as TEST_ENV parameter")
    
    # Supply the credential by running TEST_PASSSWORD=<yourpass>
    @property
    def password(self):
        return self.config_data["password"]
        if not password:
            return os.getenv("TEST_PASSWORD") # If no data from env.json, fallback to TEST_ENV parameter
            if not password:
                raise ValueError("PASSWORD not set in environment file nor provided as TEST_ENV parameter")

# Module-level instance for test environment configuration
# Run TEST_ENV=prod pytest to use this
env = os.getenv("TEST_ENV", "prod")
config = Config(env)