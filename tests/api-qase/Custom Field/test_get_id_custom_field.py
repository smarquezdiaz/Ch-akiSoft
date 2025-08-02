import pytest
import requests
import json
from config import BASE_URI,TOKEN,TOKEN_Invalido


@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC021_Obtener_un_campo_personalizado_por_ID_valido ():
    url = f"{BASE_URI}custom_field/40"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC022_Obtener_un_campo_personalizado_por_ID_vacio():
    url = f"{BASE_URI}custom_field/id"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC023_Realizar_una_solicitud_con_id_numero_negativo ():
    url = f"{BASE_URI}custom_field/-1"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC024_Realizar_una_solicitud_con_id_numero_decimal_positivo ():
    url = f"{BASE_URI}custom_field/2.5"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC025_Realizar_una_solicitud_con_id_numero_decimal_negativo():
    url = f"{BASE_URI}custom_field/-1.5"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC026_Realizar_una_solicitud_con_id_letras ():
    url = f"{BASE_URI}custom_field/-1.5"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC027_Realizar_una_solicitud_con_id_simbolos():
    url = f"{BASE_URI}custom_field/%40"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.negativa
@pytest.mark.funcional
def test_AE_TC028_Realizar_una_solicitud_con_id_que_no_existe ():
    url = f"{BASE_URI}custom_field/400"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 404, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)
