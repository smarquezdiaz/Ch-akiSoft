import pytest

from config import TOKEN
from src.assertions.get_cases_assertions import assert_response_status_code_suites
from src.assertions.get_suites_assertions import assert_get_suites_response_schema, assert_get_suites_assertion
from src.common.logger import log_api_call
from src.common.static_data_suites import StaticDataSuites


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM001_Obtener_todos_los_casos_de_prueba_con_datos_validos(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.default_url_suffix.value)
    log_api_call(method="GET",
                 url= response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(),"get_suites_response.json")
    assert_response_status_code_suites(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM002_Obtener_todos_los_casos_de_prueba_con_url_invalida(get_invalid_url, get_token):
    response = assert_get_suites_assertion(get_invalid_url, get_token, StaticDataSuites.invalid_url_suffix.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(),"not_found_response.json")
    assert_response_status_code_suites(404, response.status_code)


@pytest.mark.regression
@pytest.mark.negative
def test_SM003_Obtener_todos_los_casos_de_prueba_sin_token(get_url,get_headers):
    response = assert_get_suites_assertion(get_url, get_headers, StaticDataSuites.default_url_suffix.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "unautenthicated_response.json")
    assert_response_status_code_suites(401, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM004_Obtener_todos_los_casos_de_prueba_con_codigo_inexistente(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.non_existent_project_code.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "bad_schema_response.json")
    assert_response_status_code_suites(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM005_Obtener_todos_los_casos_de_prueba_con_codigo_de_un_caracter(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.single_char_project_code.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "bad_schema_response.json")
    assert_response_status_code_suites(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM006_Obtener_todos_los_casos_de_prueba_con_codigo_de_11_caracteres(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.eleven_char_project_code.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "bad_schema_response.json")
    assert_response_status_code_suites(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM007_Obtener_todos_los_casos_de_prueba_con_codigo_de_tipo_numerico(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.numeric_project_code.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "bad_schema_response.json")
    assert_response_status_code_suites(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM008_Obtener_todos_los_casos_de_prueba_con_codigo_vacio(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.default_url_suite.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "not_found_response.json")
    assert_response_status_code_suites(404, response.status_code)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM009_Obtener_todos_los_casos_de_prueba_con_limite_valido(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.valid_limit_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "get_suites_response.json")
    assert_response_status_code_suites(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM010_Obtener_todos_los_casos_de_prueba_con_limite_cero(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.zero_limit_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "field_invalid_response.json")
    assert_response_status_code_suites(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM011_Obtener_todos_los_casos_de_prueba_con_limite_de_101(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.one_hundred_one_limit_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "field_invalid_response.json")
    assert_response_status_code_suites(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM012_Obtener_todos_los_casos_de_prueba_con_limite_string(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.string_limit_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "field_invalid_response.json")
    assert_response_status_code_suites(400, response.status_code)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM013_Obtener_todos_los_casos_de_prueba_con_offset_valido(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.valid_offset_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "get_suites_response.json")
    assert_response_status_code_suites(200, response.status_code)

@pytest.mark.xfail
def test_SM014_Obtener_todos_los_casos_de_prueba_con_offset_fuera_de_rango(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.invalid_offset_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "get_suites_response.json")
    assert_response_status_code_suites(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM015_Obtener_todos_los_casos_de_prueba_con_offset_string(get_url, get_token):
    response = assert_get_suites_assertion(get_url, get_token, StaticDataSuites.string_offset_param.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_get_suites_response_schema(response.json(), "field_invalid_response.json")
    assert_response_status_code_suites(400, response.status_code)