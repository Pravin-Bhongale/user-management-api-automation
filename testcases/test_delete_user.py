import pytest
from api.user_api import UserAPI


@pytest.mark.parametrize("user_id", [1])
def test_delete_user_positive(user_id):
    response = UserAPI.delete_user(user_id)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 200
    assert data["data"] is None
    assert data["msg"] == "success"


@pytest.mark.parametrize("user_id", ['a', 'b'])
def test_delete_user_negative(user_id):
    response = UserAPI.delete_user(user_id)
    assert response.status_code in (400, 404)
    data = response.json()
    assert data["code"] in (400, 404)
    assert data["data"] is None
