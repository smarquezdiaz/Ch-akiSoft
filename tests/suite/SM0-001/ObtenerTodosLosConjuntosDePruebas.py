import pytest
import requests

from src.common.config import URL_SUITE, TOKEN_SOL

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_sm_tc001_Obtener_todos_los_conjuntos_de_pruebas_existentes():
    url = URL_SUITE

    token = TOKEN_SOL

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 200

    # Validar estructura

    data = response.json()
    print(data)

    assert "status" in data

def test_sm_tc002_Verificar_que_de_error_al_mandar_la_URL_mal_formada():
    url = URL_SUITE + "/list"

    token = TOKEN_SOL

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 404

def test_sm_tc003_Verificar_que_no_permita_obtener_la_lista_sin_autentificar():
    url = URL_SUITE + "/list"

    # token = TOKEN_SOL
    #
    # headers = {
    #     'Token': token,
    #     'accept': 'application/json',
    #     'content-type': 'application/json'
    # }

    response = requests.request("GET", url)

    assert response.status_code == 401