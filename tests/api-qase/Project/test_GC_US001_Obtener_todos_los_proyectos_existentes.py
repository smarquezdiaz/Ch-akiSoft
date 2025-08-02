import pytest
import requests

@pytest.mark.smoke
@pytest.mark.regression
def test_GC001_Obtener_todos_los_proyectos_existentes():
    #url = f"{get_url}/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=100&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.regression
def test_GC002_Verificar_que_se_muestre_erro_al_mandar_la_URL_mal_formada():
        # url = f"{get_url}/project"
        token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
        url = "https://api.qase.io/v1/proyect?limit=100&offset=0"

        headers = {
            'Token': token,
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        assert response.status_code == 404

@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.regression
def test_GC003_Obtener_proyectos_con_un_token_incorrecto():

        token = "3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
        url = "https://api.qase.io/v1/project?limit=100&offset=0"

        headers = {
            'Token': token,
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        assert response.status_code == 401


@pytest.mark.smoke
@pytest.mark.regression
def test_GC004_Obtener_un_solo_proyecto_con_limit_1():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=1&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

@pytest.mark.regression
def test_GC005_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_limit_con_valor_de_0():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=0&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 400 or response.status_code == 422

@pytest.mark.regression
def test_GC006_Verificar_respuesta_de_error_con_limit_como_texto_limit_abc_():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=abc&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code ==400

@pytest.mark.smoke
def test_GC007_Verificar_que_no_permita_obtener_proyectos_con_limit_5_y_offset_10():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=5&offset=10"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

@pytest.mark.regression
def test_GC008_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_negativo():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=10&offset=-5"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 400

@pytest.mark.regression
def test_GC009_Verificar_que_no_permita_obtener_proyectos_con_limit_mayor_al_máximo_limit_101():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=101&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 400 or response.status_code == 422

@pytest.mark.regression
def test_GC010_Verificar_que_no_permita_obtener_proyectos_con_limit_menor_al_limite_inferior():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=-1&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 400 or response.status_code == 422

@pytest.mark.regression
def test_GC011_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_excesivo():
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=5&offset=999999"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

@pytest.mark.smoke
def test_GC012_Verificar_que_sin_header_token_deberia_dar_error():
    url = "https://api.qase.io/v1/project?limit=10"

    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 401

@pytest.mark.regression
def test_GC013_Sin_headers_deberia_devolver_error():
    url = "https://api.qase.io/v1/project?limit=10"

    response = requests.get(url)
    assert response.status_code == 401


