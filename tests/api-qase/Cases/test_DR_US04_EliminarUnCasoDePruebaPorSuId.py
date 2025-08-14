
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
    "Este caso de prueba verifica que el sistema permita eliminar un caso de prueba existente y que la API responda con un estado HTTP 200"
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
    "Este caso de prueba verifica que después de eliminar un caso de prueba, este ya no esté disponible en el sistema de Qase, confirmando que intentos posteriores de acceso resulten en errores de no encontrado. "
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
@pytest.mark.parametrize("id_bad",[StaticDataCases.type_string.value,StaticDataCases.id_does_not_exist.value,StaticDataCases.negative_id.value,StaticDataCases.empty_id.value,StaticDataCases.special_id.value])
def test_DR_TC92_93_95_96_97_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_invalido(get_url,id_bad):
    """DR_TC92_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_string
    Este caso de prueba verifica que al intentar eliminar un caso de prueba utilizando un ID de tipo string, la API rechace la solicitud y retorne un estado HTTP 404, ya que el ID debe ser un entero válido
    DR_TC93_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_que_no_existe
    Este caso de prueba, se verifica que al intentar eliminar un caso de prueba con un ID que no existe en el sistema, la API responda con un estado HTTP 404, indicando que el recurso solicitado no fue encontrado
    DR_TC95_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_negativo
    Se comprueba que al intentar eliminar con un ID negativo en la URL, la API responda con estado HTTP 404, ya que IDs negativos no son válidos en el sistema
    DR_TC96_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_vacío
    Este caso de prueba verifica que al intentar eliminar con un ID vacío en la URL, la API retorne estado HTTP 404, indicando ruta inválida o recurso no encontrado
    DR_TC97_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_con_caracteres_especiales_string
    Se verifica que al usar un ID con caracteres especiales (como @, #, etc.) en la URL, la API responda con estado HTTP 404, ya que tales IDs no son válidos"""
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_bad),
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
@pytest.mark.xfail(raises= "el campo id solo acepta integer pero si se manda un float responde un estado 200 al eliminar un caso de prueba : DR-BUG004", run=False)
def test_DR_TC94_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_con_ID_de_tipo_float(get_url,patch_add_case):
    "Este caso de prueba evalúa que al usar un ID de tipo float en la URL para eliminación, la API retorne estado HTTP 404, ya que IDs float no son válidos"
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
def test_DR_TC98_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_que_no_existe(get_url,patch_add_case):
    "Este caso de prueba verifica que al intentar eliminar un caso de prueba en un proyecto inexistente, la API retorne estado HTTP 404, indicando que el proyecto no fue encontrado"
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
    "Se verifica que al usar una ruta mal escrita o incorrecta para la eliminación, la API responda con estado HTTP 404"
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
@pytest.mark.parametrize("token_invalid",[StaticDataHeaders.invalid_token_header.value,StaticDataHeaders.no_token_header.value])
def test_DR_TC100_101_Verificar_que_retorna_un_estado_401_al_eliminar_un_caso_de_prueba_con_un_token_invalido(get_url,patch_add_case,token_invalid):
    """DR_TC100_Verificar_que_retorna_un_estado_401_al_eliminar_un_caso_de_prueba_con_un_token_invalido
    Este caso de prueba verifica que al usar un token inválido para la eliminación, la API retorne estado HTTP 401, indicando falta de autorización
    DR_TC101_Verificar_que_retorna_un_estado_401_al_eliminar_un_caso_de_prueba_con_un_token_vacío
    Se verifica que al omitir el token o usar uno vacío en la solicitud de eliminación, la API responda con estado HTTP 401, reforzando la autenticación requerida"""
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url,  StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=token_invalid)
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
    "Este caso de prueba verifica que al usar el método PATCH en lugar de DELETE para eliminación, la API retorne estado HTTP 400"
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
@pytest.mark.parametrize("method_",[StaticDataVerbs.put.value,StaticDataVerbs.post.value])
def test_DR_TC103_Verificar_que_retorna_un_estado_405_al_eliminar_un_caso_de_prueba_con_el_método_PUT_POST(get_url,patch_add_case,method_):
    """DR_TC103_Verificar_que_retorna_un_estado_405_al_eliminar_un_caso_de_prueba_con_el_método_PUT
    Se verifica que al intentar eliminación con método PUT, la API responda con estado HTTP 405, rechazando el método
    DR_TC104_Verificar_que_retorna_un_estado_405_al_eliminar_un_caso_de_prueba_con_el_método_POST
    Se verifica que al intentar eliminación con método POST, la API responda con estado HTTP 405, rechazando el método"""
    id_created = patch_add_case["result"]["id"]
    response = request_function(method_, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=method_,
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
@pytest.mark.parametrize("title_",[StaticDataCases.title_lange.value,StaticDataCases.title_one.value])
def test_DR_TC105_106_titulo_de_un_proyecto_invalido(get_url,patch_add_case,title_):
    """DR_TC105_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_con_mas_de_10_caracteres
    Se verifica que al usar un código de proyecto con más de 10 caracteres, la API responda con 404
    DR_TC106_Verificar_que_retorna_un_estado_404_al_eliminar_un_caso_de_prueba_de_un_proyecto_con_1_solo_carácter
    Se verifica que al usar un código de proyecto con 1 caracter, la API responda con 404"""
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,
                                case_patch_join(title_, id_created),
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
