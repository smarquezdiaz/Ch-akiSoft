import json

import pytest
import requests

from config import TOKEN


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

