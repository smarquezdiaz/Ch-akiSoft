import pytest

from src.common.logger import log_api_call
from config import TOKEN,TOKEN_Invalido
from src.assertions.get_custom_field_assertions import assert_response_status_code_custom_field
from src.assertions.delete_custom_field_assertions import assert_delete_custom_field_response_schema
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.smoke
def test_AE_TC054_Eliminar_campo_con_ID_valido (get_url):
    """Descripcion:el usuario puede eliminar un campo personalizado con ID valido   """
    # Paso 1: Eliminar el campo
    field_id = StaticDataCustomField.delete_custom_field2.value
    response = request_function(
            StaticDataVerbs.delete.value,
            get_url,
            StaticDataModules.custom_field.value,
            field_id,
            StaticDataHeaders.default_header.value
        )

    log_api_call("DELETE", response.url, response.headers, None, TOKEN, response)

    assert_delete_custom_field_response_schema(response.json(), "delete_correcto")
    assert_response_status_code_custom_field(200, response.status_code)



@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC055_ID_inexistente(get_url):
    """Descripcion:el usuario no puede eliminar un campo personalizado con ID inexistente    """
    # Paso 1: Eliminar el campo
    field_id = StaticDataCustomField.delete_custom_inexistente.value
    response = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        field_id,
        StaticDataHeaders.default_header.value
    )

    log_api_call("DELETE", response.url, response.headers, None, TOKEN, response)

    assert_delete_custom_field_response_schema(response.json(), "delete_schema_salida_404")
    assert_response_status_code_custom_field(404, response.status_code)


# Datos de prueba negativos (todos con el mismo schema de error)
test_data = [
    ("AE-TC056: ID inválido tipo string", "Probar eliminación con un ID que es texto no numérico", "/a", StaticDataHeaders.default_header.value, 400),
    ("AE-TC059: ID negativo", "Probar eliminación con un ID numérico negativo", "/-123", StaticDataHeaders.default_header.value, 400),
    ("AE-TC060: ID decimal positivo", "Probar eliminación con un ID decimal positivo", "/123.45", StaticDataHeaders.default_header.value, 400),
    ("AE-TC061: ID decimal negativo", "Probar eliminación con un ID decimal negativo", "/-123.45", StaticDataHeaders.default_header.value, 400),
    ("AE-TC062: ID vacío", "Probar eliminación sin especificar un ID", "/", StaticDataHeaders.default_header.value, 400),
    ("AE-TC063: ID nulo", "Probar eliminación con un ID nulo (None)", "", StaticDataHeaders.default_header.value, 400),
    ("AE-TC064: ID extremadamente grande", "Probar eliminación con un ID demasiado grande", "/9999999999999999999999999", StaticDataHeaders.default_header.value, 400),
]
@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "test_name, description, field_id, headers, expected_status",
    test_data,
    ids=[case[0] for case in test_data]  # Solo mostramos el nombre del caso en el reporte
)
def test_delete_custom_field_negative(get_url, test_name, description, field_id, headers, expected_status):
    """
    Casos negativos de eliminación de campo personalizado.
    """
    print(f"\n[INFO] Ejecutando caso: {test_name}")
    print(f"[INFO] Descripción: {description}")

    response = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        field_id,
        headers
    )

    log_api_call("DELETE", response.url, response.headers, None, TOKEN, response)

    assert_delete_custom_field_response_schema(response.json(), "delete_schema_salida_400")
    assert_response_status_code_custom_field(expected_status, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC057_Sin_autenticacion(get_url):
    """Descripcion:el usuario no puede eliminar un campo personalizado si no tiene autenticacion     """
    # Paso 1: Eliminar el campo
    field_id = StaticDataCustomField.delete_custom_field3.value
    response = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        field_id,
        StaticDataHeaders.invalid_token_header.value
    )

    log_api_call("DELETE", response.url, response.headers, None, TOKEN_Invalido, response)

    assert_delete_custom_field_response_schema(response.json(), "delete_schema_salida_401")
    assert_response_status_code_custom_field(401, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC058_Eliminar_mismo_campo_dos_veces(get_url):
    """Verificar que al intentar eliminar un campo ya eliminado, la API responde con un error 404."""

    field_id = StaticDataCustomField.delete_custom_field4.value

    # Primer intento de eliminación (debe funcionar)
    response_first = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        field_id,
        StaticDataHeaders.default_header.value
    )

    log_api_call("DELETE", response_first.url, response_first.headers, None, TOKEN, response_first)

    assert_delete_custom_field_response_schema(response_first.json(), "delete_correcto")
    assert_response_status_code_custom_field(200, response_first.status_code)

    # Segundo intento de eliminación (debe dar 404)
    response_second = request_function(
        StaticDataVerbs.delete.value,
        get_url,
        StaticDataModules.custom_field.value,
        field_id,
        StaticDataHeaders.default_header.value
    )

    log_api_call("DELETE", response_second.url, response_second.headers, None, TOKEN, response_second)

    assert_delete_custom_field_response_schema(response_second.json(), "delete_schema_salida_404")
    assert_response_status_code_custom_field(404, response_second.status_code)
