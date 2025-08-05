import jsonschema
import pytest


from src.utils.load_resources import load_schema_resource1

def assert_post_custom_field_request_schema(payload: dict, schema_key: str):
    schema = load_schema_resource1("add_custom_field_request", schema_key)
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for payload '{schema_key}': {err}")



def assert_post_custom_field_response_schema(response,schema_key):
    schema = load_schema_resource1("add_custom_field_response", schema_key)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")
