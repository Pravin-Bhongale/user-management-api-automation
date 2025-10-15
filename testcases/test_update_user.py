import pytest
from api.user_api import UserAPI


@pytest.mark.parametrize("user_id,payload", [
    (1, {"email": "new_email@example.com"})
])
def test_update_user_positive(user_id, payload):
    response = UserAPI.update_user_email(user_id, payload)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 200
    assert data["data"] is None
    assert data["msg"] == "success"


@pytest.mark.parametrize("user_id,payload", [
    ('a', {"email": "+invalid"})   # non-existent user
])
def test_update_user_negative(user_id, payload):
    response = UserAPI.update_user_email(user_id, payload)
    assert response.status_code in (400, 404, 422)
    data = response.json()
    assert data["code"] in (400, 404, 422)
    assert data["data"] is None
