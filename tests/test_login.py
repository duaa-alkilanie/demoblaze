import json
import jsonpath
import requests
from tests.test_signUp import do_sign_up

# from tests import end_points
# defined url,path for posts,header to send with GET request
# url = end_points["url"]
url = "https://api.demoblaze.com"


def test_login_with_valid_data():
    path = "/login"
    header = {"Content-Type": "application/json"}
    username, password = do_sign_up()

    body = {
        "username": username,
        "password": password
    }
    response = requests.post(url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    print("username==", username)
    print("password==", password)
    auth_token = jsonpath.jsonpath(response_text, "Auth_token")
    status_code = response.status_code
    print(status_code)
    assert response.status_code == 200
    assert auth_token is not None


def test_login_with_invalid_password():
    path = "/login"
    header = {"Content-Type": "application/json"}

    username, password = do_sign_up()

    body = {
        "username": username,
        "password": "password"
    }
    response = requests.post(url + path, headers=header, json=body)
    response_text = json.loads(response.text)
    print("response==", response_text)
    print(response.status_code)
    print(" valid username with login ==", body["username"])
    print(" invalid password with login==", body["password"])
    erro_message = jsonpath.jsonpath(response_text, "errorMessage")
    status_code = response.status_code
    print(status_code)
    assert response.status_code == 200
    assert erro_message[0] == "Wrong password."


def do_login():
    path = "/login"
    header = {"Content-Type": "application/json"}
    username, password = do_sign_up()
    body = {
        "username": username,
        "password": password
    }
    response = requests.post(url + path, headers=header, json=body)
    return body["username"], body["password"], response
