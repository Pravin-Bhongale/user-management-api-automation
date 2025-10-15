import pytest
from api.user_api import UserAPI


@pytest.mark.parametrize("params", [
    {"page": 1, "size": 10, "keyword": "test"},
    {"page": 2, "size": 5, "keyword": ""}
])
def test_batch_query_positive(params):
    response = UserAPI.batch_query_users(params)
    assert response.status_code == 200
    data = response.json()["data"]
    assert "total" in data
    assert "list" in data
    for user in data["list"]:
        assert "id" in user
        assert "username" in user


@pytest.mark.parametrize("params", [
    {"page": -1, "size": 10},
    {"page": 1, "size": 0},
    {"page": 9999, "size": 10}  # beyond total pages
])
def test_batch_query_negative(params):
    response = UserAPI.batch_query_users(params)
    assert response.status_code in (400, 422)
    data = response.json()
    assert data["code"] in (400, 422)
    assert data["data"] is None
