import pytest

from config import TOKEN
from src.assertions.assert_suites import assert_200_schema_items, assert_not_found_route_schema_items, \
    assert_unauthenticated_schema_items, project_not_found_schema_items, assert_method_not_supported_schema_items, \
    assert_method_not_supported_and_id_empty_schema_items, suite_not_found_schema_items, \
    suite_destination_id_invalid_schema_items
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_suite.payloads_suite import create_destination_id_payload
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global
from src.utils.suites_utils import generate_random_code_project, generate_random_id_suite, \
    generate_random_destination_id


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_SM_TC038_Eliminar_un_conjunto_de_pruebas_con_un_ID_valido(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con url, header, código e id válidos, para obtener
    resultado 200.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)
    assert_200_schema_items(response.json()["result"]["id"], response.json()["status"],  id_to_delete)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC039_Eliminar_un_conjunto_de_pruebas_con_URL_base_mal_formada(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con url invalida, para obtener resultado 404.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.invalid_url_suffix_for_404.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    assert_not_found_route_schema_items(response, id_to_delete)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC040_Eliminar_un_conjunto_de_pruebas_sin_autenticacion(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, sin token, para obtener resultado 401.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.no_token_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "unautenthicated_response.json", "schema_suite")
    assert_response_status_code_global(401, response.status_code)
    assert_unauthenticated_schema_items(response)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC041_Eliminar_un_conjunto_de_pruebas_para_un_codigo_de_proyecto_inexistente(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con codigo de proyecto inexistente,
    para obtener resultado 404.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"/{generate_random_code_project(1)}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    project_not_found_schema_items(response)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC042_Eliminar_un_conjunto_de_pruebas_con_el_codigo_de_proyecto_vacio(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con el código de proyecto vacío,
     para obtener resultado 405.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"/{generate_random_code_project(0)}/{id_to_delete}", StaticDataHeaders.no_token_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(405, response.status_code)
    assert_method_not_supported_schema_items(response, id_to_delete)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC044_Eliminar_un_conjunto_de_pruebas_con_el_ID_vacio(get_url):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con el id de la url vacío,
     para obtener resultado 405.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/", StaticDataHeaders.no_token_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "not_found_response.json", "schema_suite")
    assert_response_status_code_global(405, response.status_code)
    assert_method_not_supported_and_id_empty_schema_items(response)

#Media
@pytest.mark.parametrize("id_to_delete", [-1, "a", 0.1, True, False])
@pytest.mark.regression
@pytest.mark.negative
def test_Eliminar_un_conjunto_de_pruebas_con_id_invalido(get_url, id_to_delete):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con id inválido (-1, "a", 0.1, True, False)
    , para obtener resultado 404.
    Incluye los TC:
    - SM-TC043: Verificar error al eliminar un conjunto con un ID negativo
    - SM-TC045: Verificar error al eliminar un conjunto con un ID de tipo string
    - SM-TC047: Verificar error al eliminar un conjunto con un ID de tipo flotante (0.1)
    - SM-TC048: Verificar error al eliminar un conjunto con un ID booleano true
    - SM-TC049: Verificar error al eliminar un conjunto con un ID booleano false
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    suite_not_found_schema_items(response)

#Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="Redondea el decimal a entero y si ese id entero existe elimina exitosamente")
def test_SM_TC046_Eliminar_un_conjunto_de_pruebas_con_un_ID_de_tipo_flotante(get_url):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con el id de la url con valor 3.1
     para obtener resultado 404.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{generate_random_id_suite}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert response.status_code in (404, 200)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_SM_TC050_Eliminar_un_conjunto_de_pruebas_y_mover_sus_casos_a_un_destination_id_valido(get_url, setup_add_suite, setup_add_suite_for_destination_id):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con un id de destino valido
     para obtener resultado 200.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    destination_id_payload = setup_add_suite_for_destination_id
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=destination_id_payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)
    assert_200_schema_items(response.json()["result"]["id"], response.json()["status"],  id_to_delete)

#Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="Elimina un conjunto de pruebas cuando el id de destino es string")
def test_SM_TC051_Eliminar_un_conjunto_de_pruebas_y_mover_casos_a_un_destination_id_de_tipo_string(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con un id de destino de tipo string
    para obtener resultado 404.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    destination_id_payload = create_destination_id_payload(generate_random_destination_id("string"))
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"/{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=destination_id_payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    suite_destination_id_invalid_schema_items(response)

#Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason="Elimina un conjunto de pruebas cuando el id de destino es decimal")
def test_SM_TC052_Eliminar_un_conjunto_de_pruebas_y_mover_casos_a_un_destination_id_de_tipo_flotante(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con un id de destino de tipo flotante
    para obtener resultado 404.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    destination_id_payload = create_destination_id_payload(generate_random_destination_id("float"))
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"/{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=destination_id_payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "bad_schema_response.json", "schema_suite")
    assert_response_status_code_global(404, response.status_code)
    suite_destination_id_invalid_schema_items(response)