import pytest

from config import TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM001_Obtener_todos_los_casos_de_prueba_con_datos_validos(get_url):
    response = request_function(StaticDataVerbs.get.value ,get_url, StaticDataModules.suite.value ,StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url= response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(),"get_suites_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM002_Obtener_todos_los_casos_de_prueba_con_url_invalida(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value, StaticDataSuites.invalid_url_suffix_for_404.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)


@pytest.mark.regression
@pytest.mark.negative
def test_SM003_Obtener_todos_los_casos_de_prueba_sin_token(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value,
                                StaticDataHeaders.no_token_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "unautenthicated_response.json", "schema_suite")
    assert_response_status_code_global(401, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM004_Obtener_todos_los_casos_de_prueba_con_codigo_inexistente(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.non_existent_project_code.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM005_Obtener_todos_los_casos_de_prueba_con_codigo_de_un_caracter(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.single_char_project_code.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM006_Obtener_todos_los_casos_de_prueba_con_codigo_de_11_caracteres(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.eleven_char_project_code.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM007_Obtener_todos_los_casos_de_prueba_con_codigo_de_tipo_numerico(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.numeric_project_code.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM008_Obtener_todos_los_casos_de_prueba_con_codigo_vacio(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suite.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM009_Obtener_todos_los_casos_de_prueba_con_limite_valido(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.valid_limit_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_suites_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM010_Obtener_todos_los_casos_de_prueba_con_limite_cero(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.zero_limit_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM011_Obtener_todos_los_casos_de_prueba_con_limite_de_101(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.one_hundred_one_limit_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM012_Obtener_todos_los_casos_de_prueba_con_limite_string(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.string_limit_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM013_Obtener_todos_los_casos_de_prueba_con_offset_valido(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.valid_offset_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_suites_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="valor de offset fuera de rango")
def test_SM014_Obtener_todos_los_casos_de_prueba_con_offset_fuera_de_rango(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.invalid_offset_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_suites_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM015_Obtener_todos_los_casos_de_prueba_con_offset_string(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.string_offset_param.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)