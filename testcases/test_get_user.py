import pytest
from api.user_api import UserAPI


@pytest.mark.parametrize("user_id", [1])
def test_get_user_positive(user_id):
    response = UserAPI.get_user(user_id)
    assert response.status_code == 200
    data = response.json()["data"]
    assert int(data["id"]) == user_id
    assert "username" in data
    assert "email" in data


@pytest.mark.parametrize("user_id", ['a', 'b'])
def test_get_user_negative(user_id):
    response = UserAPI.get_user(user_id)
    assert response.status_code == 404
    data = response.json()
    assert data["code"] == 404
    assert data["data"] is None
