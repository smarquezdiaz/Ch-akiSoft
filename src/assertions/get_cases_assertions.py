
import json
import os
import jsonschema
import pytest

def load_schema_resource(json_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas','schema_cases', json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)

def load_schema_resource1(json_name,schema_key=None):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', 'schema_custom_fields', f"{json_name}.json")
    with open(file_path, 'r', encoding='utf-8') as schema_file:
        all_schemas = json.load(schema_file)

    if schema_key:
        if schema_key not in all_schemas:
            raise ValueError(f"Schema '{schema_key}' no encontrado en el archivo {json_name}.json")
        return all_schemas[schema_key]

    return all_schemas

def assert_response_schema(response, json_file):
    schema = load_schema_resource(json_file)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")