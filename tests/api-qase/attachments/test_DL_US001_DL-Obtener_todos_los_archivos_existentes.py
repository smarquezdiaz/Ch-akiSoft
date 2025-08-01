import pytest
import json
import jsonschema
import requests

from config import BASE_URI,TOKEN

@pytest.mark.smoke
@pytest.mark.regression

def test_SM001_Obtener_todos_los_casos_de_prueba():

    url = f"{BASE_URI}/attachment"
    token = TOKEN
    headers = {
        'accept': 'application/json',
        'Token': token
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_SM002_Obtener_lista_de_archivos_con_un_token_invalido():

    url = "https://api.qase.io/v1/attachment"
    token = "0676837bed7d0effa596f6b154877cccea3008d2cd807a30d503dedd057b513z"
    headers = {
        'accept': 'application/json',
        'Token': token
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_SM003_Obtener_una_cierta_cantidad_de_archivos():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "limit": 1
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 200

def test_SM004_Verificar_limite_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "limit": 1111111
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM005_Verificar_limite_negativo_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "limit": -11
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM006_Colocar_letras_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "limit": "a"
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM007_Colocar_caracteres_especiales_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "limit": "·$%!"
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM008_Omitir_un_archivo():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "offset": 1
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 200

def test_SM009_Verificar_el_limite_en_el_campo_de_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "offset": 2312312312313333
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 200

def test_SM010_Verificar_limite_negativo_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "offset": -1
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM011_Colocar_letras_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "offset": "hola"
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400

def test_SM012_Colocar_caracteres_especiales_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    token = TOKEN
    payload = json.dumps({
        "offset": "·$ª()"
    })
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 400
