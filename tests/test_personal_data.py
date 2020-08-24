from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK

from mydata.personal_data import app


def test_status_should_return_200():
    client = TestClient(app)
    response = client.get("/info")
    assert response.status_code == HTTP_200_OK

def test_retun_data_in_json():
    client = TestClient(app)
    response = client.get("/info")
    assert response.headers["Content-Type"] == "application/json"

def test_response_should_be_a_list():
    client = TestClient(app)
    response = client.get("/info")
    assert isinstance(response.json(), list)