import json
import os


class Config:
    def __init__(self, env="test"):
        self.env = env
        self.load_config()

    def load_config(self):
        path = os.path.join(os.path.dirname(__file__), "../config/test_env.json")
        with open(path) as f:
            config = json.load(f)
        self.base_url = config[self.env]["base_url"]
        self.timeout = config[self.env].get("timeout", 10)


config = Config()



