import pytest
import requests
import json
from config import BASE_URI,TOKEN_Invalido
from src.headers.headers import get_header_with_token,get_header_without_token
from src.assertions.get_custom_field_assertions import assert_get_custom_field_response_schema

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC021_Obtener_un_campo_personalizado_por_ID_valido ():
    url = f"{BASE_URI}custom_field/40"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(),"custom_field_schema")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC022_Obtener_un_campo_personalizado_por_ID_vacio():
    url = f"{BASE_URI}custom_field/"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 500, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_message_schema")
@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC023_Realizar_una_solicitud_con_id_numero_negativo ():
    url = f"{BASE_URI}custom_field/-1"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC024_Realizar_una_solicitud_con_id_numero_decimal_positivo ():
    url = f"{BASE_URI}custom_field/2.5"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC025_Realizar_una_solicitud_con_id_numero_decimal_negativo():
    url = f"{BASE_URI}custom_field/-1.5"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC026_Realizar_una_solicitud_con_id_letras ():
    url = f"{BASE_URI}custom_field/-1.5"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC027_Realizar_una_solicitud_con_id_simbolos():
    url = f"{BASE_URI}custom_field/%40"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_fields_schema")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC028_Realizar_una_solicitud_con_id_que_no_existe ():
    url = f"{BASE_URI}custom_field/400"
    headers = get_header_with_token()
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 404, f"Error: status code {response.status_code}, response: {response.text}"
    assert_get_custom_field_response_schema(response.json(), "error_Not_Found")

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC029_Realizar_una_solicitud_sin_autenticacion ():
    url = f"{BASE_URI}custom_field/42"
    headers=get_header_without_token()

    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 401, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
    assert_get_custom_field_response_schema(response.json(), "error_Unauthenticated")