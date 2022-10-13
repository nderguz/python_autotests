from urllib import response
import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/13")
    assert response.status_code == 200

def test_namecheck():
    response1 = requests.get("https://petstore.swagger.io/v2/pet/13")
    assert response1.json()["name"] == "Chappie"