import jsonschema
import pytest


from src.utils.load_resources import load_schema_custom_field

def assert_get_custom_field_response_schema(response,schema_key):
    schema = load_schema_custom_field("get_custom_field_response", schema_key)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")
