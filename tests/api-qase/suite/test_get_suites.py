import logging

import pytest
import requests

from src.assertions.get_suites_assertions import assert_get_suites_response_schema, assert_get_suites_assertion

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM001_Obtener_todos_los_casos_de_prueba_con_datos_validos(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, "DEMO")
    assert_get_suites_response_schema(response.json())
    logger.info("status code: %s", response.status_code)
    logger.info("response body: %s", response.json())
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.negative
def test_SM003_Obtener_todos_los_casos_de_prueba_sin_token(get_url,get_headers):
    url = f"{get_url}/suite/DEMO"

    headers = get_headers

    response = requests.get(url, headers=headers)
    assert response.status_code == 401

@pytest.mark.regression
@pytest.mark.negative
def test_SM004_Obtener_todos_los_casos_de_prueba_con_codigo_inexistente(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, "TB")
    assert response == 404

@pytest.mark.regression
@pytest.mark.negative
def test_SM005_Obtener_todos_los_casos_de_prueba_con_codigo_de_un_caracter(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, "T")
    assert response == 404

@pytest.mark.regression
@pytest.mark.negative
def test_SM006_Obtener_todos_los_casos_de_prueba_con_codigo_de_11_caracteres(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, "TTTTTTTTTTT")
    assert response == 404

@pytest.mark.regression
@pytest.mark.negative
def test_SM007_Obtener_todos_los_casos_de_prueba_con_codigo_de_tipo_numerico(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, 111)
    assert response == 404

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("code", ["TB", "T", "TTTTTTTTTTT", 111])
def test_SM007_Obtener_todos_los_casos_de_prueba_con_codigo_variado(get_url, get_token, code):
    response = assert_get_suites_assertion(get_url, get_token, code)
    assert response == 404