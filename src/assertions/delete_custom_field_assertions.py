import jsonschema
import pytest
from src.assertions.get_custom_field_assertions import load_schema_custom_field

def assert_delete_custom_field_response_schema(response,schema_key):
    schema = load_schema_custom_field("delete_custom_field_response", schema_key)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")

