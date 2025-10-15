def assert_standard_success(resp_json):
    assert isinstance(resp_json, dict), "response is not JSON"
    assert "data" in resp_json

