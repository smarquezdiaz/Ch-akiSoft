import jsonschema
import pytest
import os
import json


def assert_get_custom_field_response_schema(response,schema_key):
    schema = load_schema_custom_field("get_custom_field_response", schema_key)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")

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

def assert_response_status_code_custom_field(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"