import json

import pytest

from config import TOKEN
from src.assertions.assert_suites import assert_200_schema_items, assert_not_found_route_schema_items, \
    assert_unauthenticated_schema_items, project_not_found_schema_items, suite_not_found_schema_items, \
    assert_patch_not_supported_schema_items, assert_empty_json_schema_items, \
    assert_data_invalid_schema_items, assert_patch_not_supported_and_id_empty_schema_items
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_suite.payloads_suite import create_request_suite_payload
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global
from src.utils.suites_utils import generate_random_code_project


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_SM_TC053_Actualizar_un_conjunto_de_pruebas_con_datos_validos(get_url, setup_add_suite, setup_get_and_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con url, header, código e id válidos, para obtener
    resultado 200.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)
    assert_200_schema_items(response.json()["result"]["id"], response.json()["status"], id_to_update)
    setup_get_and_delete_suite_by_id(response.json()["result"]["id"])

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC054_Actualizar_un_conjunto_de_pruebas_con_URL_base_mal_formada(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con url invalida, para obtener resultado 404.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.invalid_url_suffix_for_404.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    assert_not_found_route_schema_items(response, id_to_update)
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC055_Actualizar_un_conjunto_de_pruebas_sin_autenticacion(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, sin token, para obtener resultado 401.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.no_token_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "unautenthicated_response.json", "schema_suite")
    assert_response_status_code_global(401, response.status_code)
    assert_unauthenticated_schema_items(response)
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC056_Actualizar_un_conjunto_de_pruebas_para_un_codigo_de_proyecto_inexistente(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con codigo de proyecto inexistente,
    para obtener resultado 404.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"/{generate_random_code_project(1)}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    project_not_found_schema_items(response)
    setup_delete_suite_by_id(id_to_update)

@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC057_Actualizar_un_conjunto_de_pruebas_con_el_codigo_de_proyecto_vacio(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con el código de proyecto vacío,
     para obtener resultado 405.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"/{generate_random_code_project(0)}/{id_to_update}", StaticDataHeaders.no_token_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(405, response.status_code)
    assert_patch_not_supported_schema_items(response, id_to_update)
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="Permite actualizar sin el header Accept")
def test_SM_TC058_Actualizar_un_conjunto_de_pruebas_sin_el_encabezado_Accept(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, sin el encabezado accept, para obtener resultado 404.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.no_accept_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    assert_not_found_route_schema_items(response, id_to_update)
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="Permite actualizar sin el header content-type")
def test_SM_TC059_Actualizar_un_conjunto_de_pruebas_sin_el_encabezado_Content_Type (get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, sin el encabezado accept, para obtener resultado 404.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.no_content_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    assert_not_found_route_schema_items(response, id_to_update)
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC060_Actualizar_un_conjunto_de_pruebas_con_un_cuerpo_de_JSON_vacio(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, sin un body, para obtener resultado 400.
    """
    id_to_update = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert_empty_json_schema_items(response.json()["status"], response.json()["errorMessage"])
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.parametrize("title", ["", 1])
@pytest.mark.regression
@pytest.mark.negative
def test_Actualizar_un_conjunto_de_pruebas_con_un_titulo_invalido(get_url, setup_add_suite, setup_delete_suite_by_id, title):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con title inválido ("", 1)
    , para obtener resultado 400.
    Incluye los TC:
    - SM-TC061: Verificar error al actualizar un conjunto con el título vacío.
    - SM-TC062: Verificar error al actualizar un conjunto con el título de tipo numérico
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload(title)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert_data_invalid_schema_items(response.json()["status"], response.json()["errorMessage"])
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC063_Actualizar_un_conjunto_de_pruebas_con_descripcion_numerica(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con description numerica
    , para obtener resultado 400.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload(None, 1)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert_data_invalid_schema_items(response.json()["status"], response.json()["errorMessage"])
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC063_Actualizar_un_conjunto_de_pruebas_con_precondiciones_numericas(get_url, setup_add_suite, setup_delete_suite_by_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con precondiciones numerica
    , para obtener resultado 400.
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload(None, None, 1)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert_data_invalid_schema_items(response.json()["status"], response.json()["errorMessage"])
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.parametrize("parent_id", [-1, 0.1,"a", True, False, [], 9223372036854775808])
@pytest.mark.regression
@pytest.mark.negative
def test_Actualizar_un_conjunto_de_pruebas_con_un_parent_id_invalido(get_url, setup_add_suite, setup_delete_suite_by_id, parent_id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con parent_id inválido (-1, 0.1,"a", True, False, [], 9223372036854775808)
    , para obtener resultado 400.
    Incluye los TC:
    - SM-TC065: Verificar error al actualizar un conjunto con parent_id negativo
    - SM-TC066: Verificar error al actualizar un conjunto con parent_id de tipo flotante
    - SM-TC067: Verificar error al actualizar un conjunto con parent_id de tipo string
    - SM-TC068: Verificar error al actualizar un conjunto con parent_id booleano true
    - SM-TC069: Verificar error al actualizar un conjunto con parent_id booleano false
    - SM-TC070: Verificar error al actualizar un conjunto con parent_id como un array vacío
    - SM-TC071: Verificar error al actualizar un conjunto con parent_id fuera del rango de un entero
    """
    id_to_update = setup_add_suite["result"]["id"]
    payload = create_request_suite_payload(None, None, None, parent_id)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}", StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "field_invalid_response.json", "schema_suite")
    assert_response_status_code_global(400, response.status_code)
    assert_data_invalid_schema_items(response.json()["status"], response.json().get("errorMessage"))
    setup_delete_suite_by_id(id_to_update)

#Media
@pytest.mark.parametrize("id", [-1, "a",1.1,0.1, True, False])
@pytest.mark.regression
@pytest.mark.negative
def test_Actualizar_un_conjunto_de_pruebas_con_un_id_invalido(get_url, id):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con id de la url inválido (-1, "a",1.1,0.1, True, False)
    , para obtener resultado 400.
    Incluye los TC:
    SM-TC072: Verificar error al actualizar un conjunto con un ID de suite negativo
    SM-TC073: Verificar error al actualizar un conjunto con el ID de la suite vacío
    SM-TC074: Verificar error al actualizar un conjunto con un ID de suite de tipo string
    SM-TC075: Verificar error al actualizar un conjunto con un ID de suite de tipo flotante
    SM-TC076: Verificar error al actualizar un conjunto con un ID de suite de tipo flotante
    SM-TC077: Verificar error al actualizar un conjunto con un ID de suite booleano true
    SM-TC078: Verificar error al actualizar un conjunto con un ID de suite booleano false
    """
    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    suite_not_found_schema_items(response)

@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC073_Actualizar_un_conjunto_de_pruebas_con_el_id_de_suite_vacio(get_url):
    """
    Descripción: Función para actualizar un conjunto de pruebas, con el id de la suite vacío,
     para obtener resultado 405.
    """

    payload = create_request_suite_payload()
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"/{StaticDataSuites.default_url_suffix.value}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="PATCH",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(405, response.status_code)
    assert_patch_not_supported_and_id_empty_schema_items(response)

