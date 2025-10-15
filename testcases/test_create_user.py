import pytest
from api.user_api import UserAPI
from common.utils import random_username, random_email


@pytest.mark.parametrize("payload", [
    {"username": random_username(), "email": random_email(), "password": "123456"},
])
def test_create_user_positive(payload):
    response = UserAPI.create_user(payload)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 200
    assert data["data"]["username"] == payload["username"]


@pytest.mark.parametrize("payload", [
    {"username": "", "email": "invalid", "password": "123"},
    {"username": "a"*257, "email": "test@example.com", "password": "123456"},])
def test_create_user_negative(payload):
    response = UserAPI.create_user(payload)
    assert response.status_code in (400, 422)
