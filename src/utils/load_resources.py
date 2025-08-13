import json
import os
import jsonschema
import pytest
import requests

def load_schema_resource(json_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)

def load_schema_resource_by_directory_for_compare(json_name, directory):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', directory, json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)

def load_schema_custom_field(json_name,schema_key=None):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', 'schema_custom_fields', f"{json_name}.json")
    with open(file_path, 'r', encoding='utf-8') as schema_file:
        all_schemas = json.load(schema_file)

    if schema_key:
        if schema_key not in all_schemas:
            raise ValueError(f"Schema '{schema_key}' no encontrado en el archivo {json_name}.json")
        return all_schemas[schema_key]

    return all_schemas

def load_schema_resource_by_directory(json_name,directory,schema_key=None):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', directory, f"{json_name}.json")
    with open(file_path, 'r', encoding='utf-8') as schema_file:
        all_schemas = json.load(schema_file)

    if schema_key:
        if schema_key not in all_schemas:
            raise ValueError(f"Schema '{schema_key}' no encontrado en el archivo {json_name}.json")
        return all_schemas[schema_key]

    return all_schemas

def assert_response_schema(response, json_file, directory):
    schema = load_schema_resource_by_directory_for_compare(json_file, directory)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")

def assert_response_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"

def assert_response_status_code_global(expected_code, status_code):
        assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"

def assert_equals(result, expected_result):
    assert result == expected_result, f"Resultado esperado {result}, resultado obtenido {expected_result}"

def assert_get_cases_assertion(method, url, headers, payload=None):
    response = requests.request(method, url, headers=headers, data=payload)
    return response
