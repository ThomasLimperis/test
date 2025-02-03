import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    json_data = response.json()
    assert json_data["name"] == "Leanne Graham"
    assert json_data["company"]["bs"] == "harness real-time e-markets"

import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "userId": 1,
        "title": "My blog post title",
        "body": "This is the text of my latest blog post."
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 201
    assert isinstance(response.json().get("id"), int)