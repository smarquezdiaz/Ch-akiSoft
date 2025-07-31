import jsonschema
import pytest
import requests

from src.utils.load_resources import load_schema_resource


def assert_get_suites_response_schema(response):
    schema = load_schema_resource("get_suites_response.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")

def assert_get_suites_assertion(get_url, get_token, code):
    url = f"{get_url}/suite/{code}"
    token = get_token

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return response.status_code