import jsonschema
import pytest

from src.assertions.get_custom_field_assertions import load_schema_custom_field

def assert_patch_custom_field_request_schema(payload: dict, schema_key: str , expect_error=False):
    schema = load_schema_custom_field("patch_custom_field_request", schema_key)
    try:
        jsonschema.validate(instance=payload, schema=schema)
        if expect_error:
            pytest.fail("Se esperaba un error de validación, pero no ocurrió.")
        return True

    except jsonschema.exceptions.ValidationError as err:
        if expect_error:
            # Dejar que el test lo capture
            print(f"[INFO] Validación fallida como se esperaba: {err}")
            return False
        else:
             pytest.fail(f"JSON schema validation error for payload '{schema_key}': {err}")



def assert_patch_custom_field_response_schema(response,schema_key):
    schema = load_schema_custom_field("patch_custom_field_response", schema_key)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")
