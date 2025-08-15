
import pytest
import json

from src.assertions.add_custom_field_assertions import assert_post_custom_field_response_schema
from src.common.logger import log_api_call
from config import TOKEN
from src.assertions.get_custom_field_assertions import assert_response_status_code_custom_field, \
    assert_get_custom_field_response_schema
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_custom_field.payloads_custom_field import get_payload_by_id
from src.utils.api_calls import request_function

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.e2e_customfield
def test_AE_US06_Custom_Field(get_url):
    """
    Flujo completo:
    1. Crear (POST) un campo personalizado con datos válidos.
    2. Obtener (GET) el campo.
    3. Actualizar (PATCH) el campo.
    4. Obtener nuevamente (GET).
    5. Eliminar (DELETE) el campo.
    6. Intentar obtener el campo eliminado (GET) -> 404.
    """

    # 1️ CREAR
    payload_create = get_payload_by_id("AE_TCe2e")
    response_create = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.custom_field.value,
        StaticDataCustomField.valido_custom_post.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload_create)
    )
    log_api_call("POST", response_create.url, response_create.headers, payload_create, TOKEN, response_create)

    # Validar esquema y código
    assert_post_custom_field_response_schema(response_create.json(), "schema_post_e2e")
    assert_response_status_code_custom_field(response_create.status_code, 200)

    field_id = response_create.json()["result"]["id"]

    # 2️ GET inicial
    response_get_1 = request_function(
        StaticDataVerbs.get.value,
        get_url,
        StaticDataModules.custom_field.value,
        f"/{field_id}",
        StaticDataHeaders.default_header.value
    )
    log_api_call("GET", response_get_1.url, response_get_1.headers, None, TOKEN, response_get_1)

    assert_response_status_code_custom_field(response_get_1.status_code, 200)
    assert_get_custom_field_response_schema(response_get_1.json(), "schema_get_salida_e2e")

    # 3️ PATCH (actualizar título)
    payload_update = {"title": payload_create["title"] + "_modificado"}
    response_patch = request_function(
        StaticDataVerbs.patch.value,
        get_url,
        StaticDataModules.custom_field.value,
        f"/{field_id}",
        StaticDataHeaders.default_header.value,
        json.dumps(payload_update)
    )
    log_api_call("PATCH", response_patch.url, response_patch.headers, payload_update, TOKEN, response_patch)
    assert_response_status_code_custom_field(response_patch.status_code, 200)

    # 4️ GET actualizado
    response_get_2 = request_function(
        StaticDataVerbs.get.value,
        get_url,
        StaticDataModules.custom_field.value,
        f"/{field_id}",
        StaticDataHeaders.default_header.value
    )
    log_api_call("GET", response_get_2.url, response_get_2.headers, None, TOKEN, response_get_2)

    assert_response_status_code_custom_field(response_get_2.status_code, 200)
    assert_get_custom_field_response_schema(response_get_2.json(), "schema_get_salida_e2e")

    # 5️ DELETE
    response_delete = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        f"/{field_id}",
        StaticDataHeaders.default_header.value
    )
    log_api_call("DELETE", response_delete.url, response_delete.headers, None, TOKEN, response_delete)
    assert_response_status_code_custom_field(response_delete.status_code, 200)

    # 6️ GET eliminado
    response_get_deleted = request_function(
        StaticDataVerbs.get.value,
        get_url,
        StaticDataModules.custom_field.value,
        f"/{field_id}",
        StaticDataHeaders.default_header.value
    )
    log_api_call("GET", response_get_deleted.url, response_get_deleted.headers, None, TOKEN, response_get_deleted)

    assert_response_status_code_custom_field(response_get_deleted.status_code, 404)
    assert response_get_deleted.status_code == 404, (
        f"El campo no fue eliminado correctamente: {response_get_deleted.json()}"
    )
