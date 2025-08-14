import json
import pytest
from config import TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_suite.payloads_suite import assert_request_suite_payload
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM016_Crear_un_nuevo_conjunto_de_pruebas(get_url, setup_delete_suite_by_id):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_suite_by_id(response.json()["result"]["id"])


@pytest.mark.regression
@pytest.mark.negative
def test_SM017_Crear_un_nuevo_conjunto_de_pruebas_con_url_invalida(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.invalid_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM018_Crear_un_nuevo_conjunto_de_pruebas_sin_token(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.no_token_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "unautenthicated_response.json", "schema_suite")
    assert_response_status_code_global(401, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM019_Crear_un_nuevo_conjunto_de_pruebas_con_codigo_inexistente(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.non_existent_project_code.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM020_Crear_un_nuevo_conjunto_de_pruebas_con_codigo_de_un_caracter(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.single_char_project_code.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM021_Crear_un_nuevo_conjunto_de_pruebas_con_codigo_de_11_caracteres(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.eleven_char_project_code.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM022_Crear_un_nuevo_conjunto_de_pruebas_con_codigo_de_tipo_numerico(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.numeric_project_code.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM023_Crear_un_nuevo_conjunto_de_pruebas_con_codigo_vacio(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suite.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM024_Crear_un_nuevo_conjunto_de_pruebas_sin_header_accept(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suite.value, StaticDataHeaders.no_accept_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM025_Crear_un_nuevo_conjunto_de_pruebas_sin_header_content(get_url):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.no_content_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_SM026_Crear_un_nuevo_conjunto_de_pruebas_con_titulo_vacio(get_url):
    payload = assert_request_suite_payload("")
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM027_Crear_un_nuevo_conjunto_de_pruebas_con_titulo_numerico(get_url, get_token):
    payload = assert_request_suite_payload(1)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM028_Crear_un_nuevo_conjunto_de_pruebas_con_descripcion_numerica(get_url, get_token):
    payload = assert_request_suite_payload(None,1)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM029_Crear_un_nuevo_conjunto_de_pruebas_con_precondiciones_numericas(get_url, get_token):
    payload = assert_request_suite_payload(None,None,1)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM030_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_negativo(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,-1)
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code(response.status_code, 400)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM031_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_float(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,0.1)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM032_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_string(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,"a")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="No valida el valor True como parent_id")
def test_SM033_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_True(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,True)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM034_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_False(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,False)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM035_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_array_vacio(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,[])
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM036_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_rango_maximo(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,9223372036854775808)
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code(response.status_code, 400)
    assert response.json()["status"] == False

@pytest.mark.regression
@pytest.mark.negative
def test_SM037_Crear_un_nuevo_conjunto_de_pruebas_con_parent_id_rango_minimo(get_url, get_token):
    payload = assert_request_suite_payload(None,None,None,-9223372036854775809)
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code(response.status_code, 400)
    assert response.json()["status"] == False
