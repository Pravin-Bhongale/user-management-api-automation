import requests
from common.config import config


class UserAPI:
    base_url = config.base_url

    @staticmethod
    def create_user(payload):
        return requests.post(f"{UserAPI.base_url}/users", json=payload)

    @staticmethod
    def get_user(user_id):
        return requests.get(f"{UserAPI.base_url}/users/{user_id}")

    @staticmethod
    def update_user_email(user_id, payload):
        return requests.put(f"{UserAPI.base_url}/users/{user_id}", json=payload)

    @staticmethod
    def delete_user(user_id):
        return requests.delete(f"{UserAPI.base_url}/users/{user_id}")

    @staticmethod
    def batch_query_users(params=None):
        return requests.get(f"{UserAPI.base_url}/users", params=params)
