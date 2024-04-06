import jsonpath
from faker import Faker
import json
import requests

url = "https://api.demoblaze.com"
path = "/signup"
header = {"Content-Type": "application/json"}


def test_sign_up_with_valid_data():
    body = {
        "username": do_faker_name(),
        "password": do_faker_name()
    }
    response = requests.post(url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    print("username==", body["username"])
    print("password==", body["password"])
    status_code = response.status_code
    print("status code== ", status_code)

    assert response.status_code == 200


def test_sign_up_with_data_already_exist(username="duaatesting", password="alkilani"):
    body = {
        "username": username,
        "password": password
    }
    response = requests.post(url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    print("username==", body["username"])
    print("password==", body["password"])
    status_code = response.status_code
    print("status code== ", status_code)
    erro_message = jsonpath.jsonpath(response_text, "errorMessage")
    assert erro_message[0] == "This user already exist."
    assert response.status_code == 200


def do_sign_up():
    body = {
        "username": do_faker_name(),
        "password": do_faker_name()
    }
    response = requests.post(url + path, headers=header, json=body)
    print("username from signup==", body["username"])
    print("password from signup==", body["password"])

    return body["username"], body["password"]


def do_faker_name():
    # Create a Faker instance
    fake = Faker()

    # Generate a fake name
    fake_name = fake.name()

    print(fake_name)
    return fake_name
