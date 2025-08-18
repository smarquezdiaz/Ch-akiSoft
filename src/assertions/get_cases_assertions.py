
import json
import os
import jsonschema
import pytest

def assert_schema_resource(json_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas','schema_cases', json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)

def assert_response_not_empty(response):
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True

def assert_response_error_not_empty(response):
    assert response.json()["message"] is not None
    assert response.json()["errors"] is not None

def assert_response_error_status_not_empty(response):
    assert response.json()["status"] == False
    assert response.json()["errorMessage"] is not None

def assert_response_error_token(response):
    assert response.json()["error"] is not None

def assert_response_error_message(response):
    assert response.json()["message"] is not None

def assert_get_cases_response_schema(response, json_file):
    schema = assert_schema_resource(json_file)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")

def assert_entities_field_equal (response , search, attribute):
    entities = response.json()["result"]["entities"]
    assert entities, "No hay casos de prueba registrados"
    for counter in entities:
        if counter[attribute] != search:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {counter['id']} tiene {attribute}={counter[f'{attribute}']} "
            )

def assert_response_status_code_case(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"