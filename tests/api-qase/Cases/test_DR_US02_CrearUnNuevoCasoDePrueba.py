
import pytest
import json
from src.conftest import get_url, get_token
from src.common.logger import log_api_call
from src.assertions.get_cases_assertions import assert_request_payload, assert_response_status_code, assert_get_cases_assertion, cases_get_url, cases_headers, assert_get_cases_response_schema

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC23_Verificar_la_creación_de_un_caso_de_prueba_con_todos_los_campo_llenos(get_url,get_token):
    request= assert_request_payload("prueba definitiva2XD", 5, 2,3,0,0)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response= assert_get_cases_assertion("POST", cases_get_url(get_url,"DEMO"), cases_headers(get_token), json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"post_cases_schema_response.json")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC24_Verificar_la_creación_de_un_caso_de_prueba_con_los_requerimientos_mínimos(get_url,get_token):
    request = assert_request_payload(title="solo titulo")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.regression
def test_DR_TC25_Verificar_que_retorna_una_respuesta_400_al_crear_un_caso_de_prueba_con_un_esquema_erróneo(get_token,get_url):
    request = assert_request_payload(title="solo titulo esquema mal",no_existe="3f23g34b34")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC26_Verificar_que_retorna_una_respuesta_401_al_crear_un_caso_de_prueba_cuando_no_tiene_un_token_valido(get_url):
    request = assert_request_payload(title="solo titulo token")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers("no autorizado"),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers("no autorizado"),
                 payload=request,
                 token="no autorizado",
                 response=response
                 )
    assert_response_status_code(response.status_code, 401)

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC27_Verificar_que_retorna_una_respuesta_404_al_crear_un_caso_de_prueba_en_un_proyecto_que_no_existe(get_url,get_token):
    request = assert_request_payload(title="solo titulo")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "No existe este proyecto"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 404)


@pytest.mark.regression
def test_DR_TC28_Verificar_que_retorna_una_respuesta_400_al_crear_un_casos_de_prueba_con_el_método_GET(get_url,get_token):
    request = assert_request_payload(title="solo titulo deberia dar 400")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)

@pytest.mark.regression
def test_DR_TC29_Verificar_que_retorna_una_respuesta_405_al_crear_un_caso_de_prueba_con_el_método_PUT(get_token,get_url):
    request = assert_request_payload(title="solo titulo")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("PUT", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="PUT",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)

@pytest.mark.regression
def test_DR_TC30_Verificar_que_retorna_una_respuesta_405_al_crear_un_caso_de_prueba_con_el_método_DELETE(get_url,get_token):
    request = assert_request_payload(title="solo titulo")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("DELETE", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="DELETE",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC31_Verificar_que_retorna_una_respuesta_405_al_crear_un_caso_de_prueba_con_campos_vacíos(get_url,get_token):
    request = assert_request_payload(title="solo titulo")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("DELETE", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="DELETE",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC32_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_severidad(get_url,get_token):
    request = assert_request_payload(title="solo titulo",severity="texto")
    #assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC33_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_prioridad(get_url,get_token):
    request = assert_request_payload(title="solo titulo",priority="texto")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC34_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_tipo(get_url,get_token):
    request = assert_request_payload(title="solo titulo",type_="texto")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC35_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_status(get_url,get_token):
    request = assert_request_payload(title="solo titulo",status="texto")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC36_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_solo_texto_para_status_de_automatización(get_url,get_token):
    request = assert_request_payload(title="solo titulo",status="texto")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC37_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_titulo_largo_mas_de_255_caracteres(get_url,get_token):
    request = assert_request_payload(title="Para crear datos aleatorios en Python, se utiliza el módulo random. Este módulo ofrece varias "
                                           "funciones para generar números aleatorios, enteros o flotantes, y para elegir elementos aleatorios "
                                           "de secuencias. La función randint(a, b) genera un entero aleatorio")
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC38_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_una_severidad_que_no_existe(get_url,get_token):
    request = assert_request_payload(title="solo titulo", severity=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC39_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_una_prioridad_que_no_existe(get_token,get_url):
    request = assert_request_payload(title="solo titulo", priority=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC40_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_tipo_que_no_existe(get_url,get_token):
    request = assert_request_payload(title="solo titulo", type_=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC41_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_un_status_que_no_existe(get_url,get_token):
    request = assert_request_payload(title="solo titulo", status=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC42_Verificar_que_retorna_una_respuesta_422_al_crear_un_caso_de_prueba_con_valor_de_status_de_automatización_que_no_existe(get_url,get_token):
    request = assert_request_payload(title="solo titulo", automation=10000)
    assert_get_cases_response_schema(request, "post_cases_schema_request.json")
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token),
                                          json.dumps(request))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=request,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 422)