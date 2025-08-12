
import random
import pytest
import json
from tests.conftest import get_url, get_token, post_resource_case
from src.common.logger import log_api_call
from src.common.static_data_cases import StaticDataCases
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.common.url import get_url_parametrized
from src.headers.headers import get_header_with_token, get_header_with_invalid_token
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_status_code
from src.assertions.get_cases_assertions import assert_get_cases_response_schema
from src.resources.payloads.payloads_case.payloads_post_case import assert_request_payload, name_random_cases

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC023_Verificar_la_creación_de_un_caso_de_prueba_con_todos_los_campo_llenos(get_url,get_token,post_resource_case):
    request= assert_request_payload(name_random_cases(), random.choice([2,3,4,5]), random.choice([1,2,3]),random.choice([2,3,8]),random.choice([0,1,2]),random.choice([0,2]))
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"post_cases_schema_response.json")

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC024_Verificar_la_creación_de_un_caso_de_prueba_con_los_requerimientos_mínimos(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(raises= "error si se manda un post con un esquema erroneo, el sistema devuelve un status 200 : DR-BUG002")
def test_DR_TC025_Verificar_que_retorna_una_respuesta_400_al_crear_un_caso_de_prueba_con_un_esquema_erróneo(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),no_existe="3f23g34b34")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC026_Verificar_que_retorna_una_respuesta_401_al_crear_un_caso_de_prueba_cuando_no_tiene_un_token_valido(get_url):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.invalid_token_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_invalid_token(),
                 payload=request,
                 token=get_header_with_invalid_token()["Token"],
                 response=response
                 )
    assert_response_status_code(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC027_Verificar_que_retorna_una_respuesta_404_al_crear_un_caso_de_prueba_en_un_proyecto_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,"/proyecto_que_no_existe",
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,"/proyecto_que_no_existe"),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC028_Verificar_la_creación_de_un_caso_de_prueba_con_severidad_critica(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),severity=StaticDataCases.severity_critical_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC029_Verificar_que_retorna_una_respuesta_405_al_crear_un_caso_de_prueba_con_el_método_PUT(get_url,get_token):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.put.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method="PUT",
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC030_Verificar_que_retorna_una_respuesta_405_al_crear_un_caso_de_prueba_con_el_método_DELETE(get_url,get_token):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method="DELETE",
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC031_Verificar_que_retorna_una_respuesta_400_al_crear_un_caso_de_prueba_con_campos_vacíos(get_url,get_token):
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload={})
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload={},
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_schema_400.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC032_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_severidad(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(),severity="texto")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC033_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_prioridad(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(),priority="texto")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC034_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_tipo(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(),type_="texto")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC035_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_status(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(),status="texto")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC036_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_status_de_automatización(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(),automation="texto")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC037_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_titulo_largo_mas_de_255_caracteres(get_url,get_token):
    request = assert_request_payload(title="Para crear datos aleatorios en Python, se utiliza el módulo random. Este módulo ofrece varias "
                                           "funciones para generar números aleatorios, enteros o flotantes, y para elegir elementos aleatorios "
                                           "de secuencias. La función randint(a, b) genera un entero aleatorio")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC038_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_una_severidad_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(), severity=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC039_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_una_prioridad_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(), priority=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC040_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_tipo_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(), type_=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC041_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_status_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(), status=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC042_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_de_status_de_automatización_que_no_existe(get_url,get_token):
    request = assert_request_payload(title=name_random_cases(), automation=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC043_Verificar_la_creación_de_un_caso_de_prueba_con_severidad_mayor(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),severity=StaticDataCases.severity_major_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC044_Verificar_la_creación_de_un_caso_de_prueba_con_severidad_normal(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),severity=StaticDataCases.severity_normal_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC045_Verificar_la_creación_de_un_caso_de_prueba_con_severidad_menor(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),severity=StaticDataCases.severity_minor_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC046_Verificar_la_creación_de_un_caso_de_prueba_con_prioridad_alta(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),priority=StaticDataCases.priority_high_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC047_Verificar_la_creación_de_un_caso_de_prueba_con_prioridad_media(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),priority=StaticDataCases.priority_medium_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC048_Verificar_la_creación_de_un_caso_de_prueba_con_prioridad_baja(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),priority=StaticDataCases.priority_low_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC049_Verificar_la_creación_de_un_caso_de_prueba_con_estatus_actual(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),status=StaticDataCases.status_actual_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC050_Verificar_la_creación_de_un_caso_de_prueba_con_estatus_draft(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),status=StaticDataCases.status_draft_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC051_Verificar_la_creación_de_un_caso_de_prueba_con_estatus_deprecated(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),status=StaticDataCases.status_deprecated_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC052_Verificar_la_creación_de_un_caso_de_prueba_con_estatus_automatizado(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),automation=StaticDataCases.automation_automated_to_be_automated_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC053_Verificar_la_creación_de_un_caso_de_prueba_con_estatus_no_automatizado(get_url,get_token,post_resource_case):
    request = assert_request_payload(title=name_random_cases(),automation=StaticDataCases.automation_is_not_automated_value.value)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    post_resource_case["created_id"] = response.json().get("result", {}).get("id")
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")