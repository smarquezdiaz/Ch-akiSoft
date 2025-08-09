import jsonschema
import pytest

from src.utils.load_resources import load_schema_resource


def assert_get_suites_response_schema(response, json_file):
    schema = load_schema_resource(json_file)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match: {err}")