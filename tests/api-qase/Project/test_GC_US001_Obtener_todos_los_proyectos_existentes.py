import pytest
import requests

from config import BASE_URI, TOKEN
from src.assertions.get_project_assertions import assert_get_project_assertion, assert_get_project_response_schema
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.headers.headers import get_header_with_token
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GC001_Obtener_todos_los_proyectos_existentes(get_url):
    # setup y teardown
    response = request_function(StaticDataVerbs.get.value ,get_url, StaticDataModules.project.value ,StaticDataProject.valid_limit_param.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url= response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)


#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GC002_Verificar_que_se_muestre_error_al_mandar_la_URL_mal_formada(get_url):
        response = request_function(StaticDataVerbs.get.value ,get_url, StaticDataModules.project.value ,StaticDataProject.invalid_url_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url= response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
        assert_response_status_code_global(404, response.status_code)

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC003_Obtener_proyectos_con_un_token_incorrecto(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_limit_param.value, StaticDataHeaders.invalid_token_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error401_project_response.json", "schemas_project")
    assert_response_status_code_global(401, response.status_code)


#Media
@pytest.mark.positive
@pytest.mark.regression
def test_GC004_Obtener_un_solo_proyecto_con_limit_1(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit1_param0.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

#media
@pytest.mark.negative
@pytest.mark.regression
def test_GC005_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_limit_con_valor_de_0(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit0_param0.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC006_Verificar_respuesta_de_error_con_limit_como_texto_limit_abc(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit_abc_param0.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)

#media
@pytest.mark.negative
@pytest.mark.regression
def test_GC007_Verificar_que_no_permita_obtener_proyectos_con_limit_5_y_offset_10(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_limit5_param10.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC008_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_negativo(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit10_param_1.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC009_Verificar_que_no_permita_obtener_proyectos_con_limit_mayor_al_máximo_limit_101(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit101_param0.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC010_Verificar_que_no_permita_obtener_proyectos_con_limit_menor_al_limite_inferior(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit_1_param0.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)

#Alta
@pytest.mark.xfail(reason="No deberia admitir un offset tan extenso")
@pytest.mark.negative
@pytest.mark.regression
def test_GC011_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_excesivo(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.invalid_limit5_param9999999.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error400_project_response.json", "schemas_project")
    assert_response_status_code_global(400, response.status_code)

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC012_Verificar_que_sin_token_debe_dar_error_sin_autentificaion(get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_limit_param.value, StaticDataHeaders.no_token_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error401_project_response.json", "schemas_project")
    assert_response_status_code_global(401, response.status_code)


