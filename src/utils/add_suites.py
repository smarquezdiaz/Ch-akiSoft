import json
import random
import string
import requests
import pytest

from config import TOKEN


def assert_add_suites_assertion(get_url, get_token, code, payload):
    url = f"{get_url}{code}"
    headers = get_token
    response = requests.post(url, headers=headers, json=payload)
    return response


def assert_request_suite_payload(
        title: str | int | None = None,
        description: str | int | None = None,
        preconditions: str | int | None = None,
        parent_id: str | int | float | list | None = None
) -> dict:
    actual_title = get_random_title() if title is None else title

    payload = {
        "title": actual_title,
        "description": get_random_property() if description is None else description,
        "preconditions": get_random_property() if preconditions is None else preconditions,
    }

    if parent_id is not None:
        payload["parent_id"] = parent_id

    return payload


def get_random_title():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return random_string

def get_random_property():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    return random_string

@pytest.fixture(scope="module")
def setup_suites_assertion():
    print("crear proyecto")
    url = "https://api.qase.io/v1/project"
    token = TOKEN

    payload_data = {
        "title": "eeeee",
        "code": "eeee",
        "description": "mmm lolo",
        "access": "all"
    }

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
    response = requests.post(url, headers=headers, data=payload)

    yield response.json()["result"]["code"]
    print("eliminar proyecto")

