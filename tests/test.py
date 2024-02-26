from currency import USD_CAD, data
import requests

response = requests.get(url=USD_CAD)

def test_url_status():
    assert response.status_code == 200


def test_json():
    assert data > 0
