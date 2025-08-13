
from tests.conftest import get_url
from src.common.logger import log_api_call
from src.common.static_data_cases import StaticDataCases
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.utils.api_calls import request_function
from src.assertions.get_cases_assertions import *
from src.resources.payloads.payloads_case.payloads_post_case import decimal_number
from src.common.url import case_patch_join


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC90_Verificar_que_se_retorna_estado_200_al_eliminar_un_caso_de_prueba(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload= None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC91_Verificar_que_el_caso_de_prueba_eliminado_ya_no_existe_en_el_sistema(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)
    response_get = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value,
                                    case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                    header_type=StaticDataHeaders.default_header.value)
    assert_response_status_code_case(response_get.status_code, 404)
    assert_get_cases_response_schema(response_get.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response_get)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC92_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_string(get_url):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, StaticDataCases.type_string.value),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC93_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_que_no_existe(get_url):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value,
                                                StaticDataCases.id_does_not_exist.value),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC94_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_float(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, decimal_number(id_created)),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC95_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_negativo(get_url):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value,
                                                StaticDataCases.negative_id.value),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC96_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_vacío(get_url):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value,
                                                StaticDataCases.empty_id.value),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC97_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_con_caracteres_especiales_string(get_url):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value,
                                                StaticDataCases.special_id.value),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC98_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataCases.project_does_not_exist.value,id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC99_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_un_ruta_mal_escrita(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataCases.empty_title.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_message.json")
    assert_response_error_message(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC100_Verificar_que_retorna_un_estado_401_al_eliminar_un_caso_de_prueba_con_un_token_invalido(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url,  StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.invalid_token_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")
    assert_response_error_token(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC101_Verificar_que_retorna_un_estado_401_al_eliminar_un_caso_de_prueba_con_un_token_vacío(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.no_token_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")
    assert_response_error_token(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC102_Verificar_que_retorna_un_estado_400_al_eliminar_un_caso_de_prueba_con_el_método_PATCH(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_schema_400.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC103_Verificar_que_retorna_un_estado_405_al_eliminar_un_caso_de_prueba_con_el_método_PUT(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.put.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.put.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")
    assert_response_error_message(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC104_Verificar_que_retorna_un_estado_405_al_eliminar_un_caso_de_prueba_con_el_método_POST(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.post.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")
    assert_response_error_message(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC105_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_con_mas_de_10_caracteres(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataCases.title_lange.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC106_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_con_1_solo_carácter(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataCases.title_one.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)