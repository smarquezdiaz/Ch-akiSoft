import pytest
import requests

from src.common.logger import log_api_call
from config import BASE_URI,TOKEN,TOKEN_Invalido
from src.headers.headers import get_header_with_token,get_header_without_token
from src.assertions.get_custom_field_assertions import assert_get_custom_field_response_schema
from src.utils.headers_custom_field import custom_field_url
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC021_Obtener_un_campo_personalizado_por_ID_valido ():
    field_id = 40
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
            token=TOKEN,
        response=response
    )

    assert response.status_code == 200
    assert_get_custom_field_response_schema(response.json(),"custom_field_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC022_Obtener_un_campo_personalizado_por_ID_vacio():
    field_id = ""
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 500
    assert_get_custom_field_response_schema(response.json(), "error_message_schema")
@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC023_Realizar_una_solicitud_con_id_numero_negativo ():
    field_id = -1
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC024_Realizar_una_solicitud_con_id_numero_decimal_positivo ():
    field_id = 0.5
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC025_Realizar_una_solicitud_con_id_numero_decimal_negativo():
    field_id = -0.9
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC026_Realizar_una_solicitud_con_id_letras ():
    field_id ="a"
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC027_Realizar_una_solicitud_con_id_simbolos():
    field_id = "@"
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC028_Realizar_una_solicitud_con_id_que_no_existe ():
    field_id = 5000
    url = custom_field_url(BASE_URI, field_id)
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 404
    assert_get_custom_field_response_schema(response.json(), "error_Not_Found")

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.regression
def test_AE_TC029_Realizar_una_solicitud_sin_autenticacion ():
    field_id = 50
    url = custom_field_url(BASE_URI, field_id)
    headers=get_header_without_token()
    response = requests.request("GET", url, headers=headers)
    log_api_call(
        method="GET",
        url=url,
        headers=headers,
        payload=None,
        token=TOKEN_Invalido,
        response=response
    )
    assert response.status_code == 401
    assert_get_custom_field_response_schema(response.json(), "error_Unauthenticated")