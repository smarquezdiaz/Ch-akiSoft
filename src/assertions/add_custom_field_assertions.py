import pytest
import json
import uuid
from jsonschema import validate, exceptions
from src.utils.api_calls import request_function
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.assertions.get_custom_field_assertions import load_schema_custom_field

def assert_post_custom_field_request_schema(payload: dict, schema_key: str , expect_error=False):
    schema = load_schema_custom_field("add_custom_field_request", schema_key)
    try:
        validate(instance=payload, schema=schema)
        if expect_error:
            pytest.fail("Se esperaba un error de validación, pero no ocurrió.")
        return True

    except exceptions.ValidationError as err:
        if expect_error:
            # Dejar que el test lo capture
            raise
        else:
             pytest.fail(f"JSON schema validation error for payload '{schema_key}': {err}")



def assert_post_custom_field_response_schema(response,schema_key):
    schema = load_schema_custom_field("add_custom_field_response", schema_key)
    try:
        validate(instance=response, schema=schema)
        return True
    except exceptions.ValidationError as err:
        pytest.fail(f"JSON schema validation error for '{schema_key}': {err}")


def crear_campo_personalizado(get_url, nombre=None):
    """Crea un campo personalizado y retorna su ID"""
    if not nombre:
        nombre = f"Campo prueba {uuid.uuid4()}"
    payload = {
        "title": nombre,
        "entity": 0,
        "type": 2
    }

    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.custom_field.value,
        "",
        StaticDataHeaders.default_header.value,
        payload=json.dumps(payload)
    )

    if response.status_code != 200:
        raise Exception(f"No se pudo crear el campo: {response.status_code} - {response.text}")

    response_data = response.json()
    return response_data["result"]["id"]