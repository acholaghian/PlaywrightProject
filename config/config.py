import json
import os


class Config:
    def __init__(self, env):
        self.env = env
        self.config_data = self._load_env_json()

    def _load_env_json(self):
        env_path = os.path.join(os.path.dirname(__file__), "env.json")
        with open(env_path, "r") as file:
            data = json.load(file)
        return data[self.env]

    # Get base URL for the website from the env.json file, or from TEST_ENV as fallback
    @property
    def base_url(self):
        base_url = self.config_data.get("base_url")
        if not base_url:
            base_url = os.getenv("TEST_BASEURL")
        if not base_url:
            raise ValueError("Base URL not set in config or TEST_BASEURL")
        return base_url

    # Getting username from env.json file, or from TEST_ENV as fallback
    @property
    def username(self):
        username = self.config_data.get("username")
        if not username:
            username = os.getenv("TEST_USERNAME")
        if not username:
            raise ValueError("Username not set in config or TEST_USERNAME")
        return username

    # Get password from the env.json file, or from TEST_ENV as fallback
    @property
    def password(self):
        password = self.config_data.get("password")
        if not password:
            password = os.getenv("TEST_PASSWORD")
        if not password:
            raise ValueError("Password not set in config or TEST_PASSWORD")
        return password


# Module-level instance for test environment configuration
# Run TEST_ENV=prod pytest to use this
env = os.getenv("TEST_ENV", "prod")
config = Config(env)
