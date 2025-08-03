import jsonschema
import pytest
import requests
from requests import Response

from src.utils.load_resources import load_schema_resource


def assert_get_cases_response_schema(response):
    schema = load_schema_resource("bad_schema_response.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")

def assert_get_cases_assertion(get_url, get_token, code):
    url = f"{get_url}/case/{code}"
    token = get_token

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return response

def assert_entities_field_equal (response , search, attribute):
    entities = response.json()["result"]["entities"]
    # dependecia a que por lo menos 1 caso de prueba este creado con el atributo que se busca
    assert entities, "No hay casos de prueba registrados"
    for counter in entities:
        if counter[attribute] != search:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {counter['id']} tiene {attribute}={counter[f'{attribute}']} "
            )


def assert_response_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Estatus esperado {status_code}, estatus obtenido {expected_code}"

def assert_equals(result, expected_result):
    assert result == expected_result, f"Resultado esperado {result}, resultado obtenido {expected_result}"