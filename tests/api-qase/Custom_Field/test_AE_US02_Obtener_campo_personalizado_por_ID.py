import pytest
from src.utils.load_resources import  assert_response_status_code_global
from src.common.logger import log_api_call
from config import TOKEN,TOKEN_Invalido
from src.assertions.get_custom_field_assertions import assert_get_custom_field_response_schema
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC021_Obtener_un_campo_personalizado_por_ID_valido (get_url):

    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_field.value, StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(),"custom_field_schema")
    assert_response_status_code_global(200, response.status_code)


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC022_Obtener_un_campo_personalizado_por_ID_vacio(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.vacio_custom_field.value, StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC023_Realizar_una_solicitud_con_id_numero_negativo (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.negativo_custom_field.value, StaticDataHeaders.default_header.value)

    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC024_Realizar_una_solicitud_con_id_numero_decimal_positivo (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value, StaticDataCustomField.decimal_positivo_custom_field.value,StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC025_Realizar_una_solicitud_con_id_numero_decimal_negativo(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value, StaticDataCustomField.decimal_negativo_custom_field.value,StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC026_Realizar_una_solicitud_con_id_letras (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.letras_custom_field.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)
@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC027_Realizar_una_solicitud_con_id_simbolos(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.simbolo_custom_field.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")
    assert_response_status_code_global(400, response.status_code)
@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC028_Realizar_una_solicitud_con_id_que_no_existe (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,StaticDataCustomField.no_existe_custom_field.value,StaticDataHeaders.default_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN,
        response=response
    )


    assert_get_custom_field_response_schema(response.json(), "error_Not_Found")
    assert_response_status_code_global(404, response.status_code)
@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC029_Realizar_una_solicitud_sin_autenticacion (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.custom_field.value,StaticDataCustomField.sin_autenticar_custom_field.value,StaticDataHeaders.invalid_token_header.value)
    log_api_call(
        method="GET",
        url=response.url,
        headers=response.headers,
        payload=None,
        token=TOKEN_Invalido,
        response=response
    )

    assert_get_custom_field_response_schema(response.json(), "error_Unauthenticated")
    assert_response_status_code_global(401, response.status_code)