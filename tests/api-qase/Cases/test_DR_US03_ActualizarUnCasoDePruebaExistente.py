
import pytest
import json
from tests.conftest import get_url
from src.common.logger import log_api_call
from src.common.static_data_cases import StaticDataCases
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.utils.api_calls import request_function
from src.assertions.get_cases_assertions import assert_get_cases_response_schema, assert_response_not_empty, assert_response_status_code_case, assert_response_error_not_empty, assert_response_error_status_not_empty, assert_response_error_token
from src.resources.payloads.payloads_case.payloads_post_case import case_request_payload, name_random_cases, random_severity_case, random_status_case, random_type_case, random_priority_case, random_automation_case, decimal_number
from src.common.url import case_patch_join

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC54_Verificar_que_se_retorna_estado_200_al_actualizar_solo_un_campo_title_de_un_caso_de_prueba(get_url,patch_add_case):
    "Este caso de prueba verifica que el sistema permita actualizar el campo de título (title) de un caso de prueba existente en un proyecto de Qase"
    id_created=patch_add_case["result"]["id"]
    request=case_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC55_Verificar_que_se_retorna_estado_200_al_actualizar_todos_los_campos_de_un_caso_de_prueba(get_url,patch_add_case):
    "Este caso de prueba verifica que el sistema permita actualizar los campos título, severidad, prioridad, tipo, status y status de automatización"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(name_random_cases(), random_severity_case(), random_priority_case(),
                                   random_type_case(), random_status_case(), random_automation_case())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("value_severity",[StaticDataCases.severity_critical_value.value,StaticDataCases.severity_major_value.value,StaticDataCases.severity_normal_value.value,StaticDataCases.severity_minor_value.value])
def test_DR_TC56_57_58_59_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba(get_url,patch_add_case,value_severity):
    """DR_TC56_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_crítico_retorne_un_estado_200
    Este caso de prueba comprueba que al actualizar el campo de severidad de un caso de prueba existente a crítico
    DR_TC57_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_mayor_retorne_un_estado_200
    Este caso de prueba comprueba que al actualizar el campo de severidad de un caso de prueba existente a mayor
    DR_TC58_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_normal_retorne_un_estado_200
    Este caso de prueba comprueba que al actualizar el campo de severidad de un caso de prueba existente a normal
    DR_TC59_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_menor_retorne_un_estado_200
    Este caso de prueba comprueba que al actualizar el campo de severidad de un caso de prueba existente a menor"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases(), severity=value_severity)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("value_priority",[StaticDataCases.priority_medium_value.value,StaticDataCases.priority_low_value.value,StaticDataCases.priority_high_value.value])
def test_DR_TC60_61_62_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba(get_url,patch_add_case,value_priority):
    """DR_TC60_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_medio_retorne_un_estado_200
    verifica la actualización del campo prioridad a "medio" en un caso de prueba y que responda un estado HTTP 200
    DR_TC61_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_bajo_retorne_un_estado_200
    verifica la actualización del campo prioridad a "bajo" en un caso de prueba y que responda un estado HTTP 200
    DR_TC62_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_alto_retorne_un_estado_200
    verifica la actualización del campo prioridad a "alto" en un caso de prueba y que responda un estado HTTP 200"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases(), priority=value_priority)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("value_type",[StaticDataCases.type_regression_value.value,StaticDataCases.type_functional_value.value,StaticDataCases.type_smoke_value.value])
def test_DR_TC63_64_65_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba(get_url,patch_add_case,value_type):
    """DR_TC63_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_regresión_retorne_un_estado_200
    En este caso de prueba, se verifica que el cambio del campo tipo a "regresión", con la API retornando estado HTTP 200
    DR_TC64_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_funcional_retorne_un_estado_200
    En este caso de prueba, se verifica que el cambio del campo tipo a "funcional", con la API retornando estado HTTP 200
    DR_TC65_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_smoke_retorne_un_estado_200
    En este caso de prueba, se verifica que el cambio del campo tipo a "smoke", con la API retornando estado HTTP 200"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases(), type_=value_type)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("value_status",[StaticDataCases.status_draft_value.value,StaticDataCases.status_deprecated_value.value,StaticDataCases.status_actual_value.value])
def test_DR_TC66_67_68_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba(get_url,patch_add_case,value_status):
    """DR_TC66_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_draft_retorne_un_estado_200
    Este caso de prueba verifica la actualización del campo status a "draft", asegurando que la API procese el cambio y responda con estado HTTP 200
    DR_TC67_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_deprecated_retorne_un_estado_200
    Este caso de prueba verifica la actualización del campo status a "deprecated", asegurando que la API procese el cambio y responda con estado HTTP 200
    DR_TC68_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_actual_retorne_un_estado_200
    Este caso de prueba verifica la actualización del campo status a "actual", asegurando que la API procese el cambio y responda con estado HTTP 200"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases(), status=value_status)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC69_Verificar_que_la_actualización_del_campo_title_con_un_solo_caracter_retorne_un_estado_200(get_url,patch_add_case):
    "Este caso de prueba verifica que la actualización del campo title a un solo carácter sea permitida, con respuesta HTTP 200"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=StaticDataCases.title_one.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize("value_automation",[StaticDataCases.automation_is_not_automated_value.value,StaticDataCases.automation_automated_to_be_automated_value.value])
def test_DR_TC70_71_Verificar_que_la_actualización_del_campo_automatización_de_un_caso_de_prueba(get_url,patch_add_case,value_automation):
    """DR_TC70_Verificar_que_la_actualización_del_campo_automatización_de_un_caso_de_prueba_a_no_automatización_retorne_un_estado_200
    Este caso de prueba verifica la actualización del campo automatización a "no automatizado", asegurando que la API procese el cambio y responda con estado HTTP 200
    DR_TC71_Verificar_que_la_actualización_del_campo_automatización_de_un_caso_de_prueba_a_automatización_retorne_un_estado_200
    Este caso de prueba verifica la actualización del campo automatización a "automatizado", asegurando que la API procese el cambio y responda con estado HTTP 200"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases(), automation=value_automation)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(), "post_cases_schema_response.json")
    assert_response_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC72_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_el_campo_nombre_vacío(get_url,patch_add_case):
    "Este caso de prueba comprueba que al intentar actualizar un caso de prueba con el campo nombre (title) vacío, la API rechace la solicitud y retorne un estado HTTP 422, indicando que la entidad no es procesable debido a la ausencia de un campo obligatorio"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=StaticDataCases.empty_title.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")
    assert_response_error_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC73_Verificar_que_retorna_error_estado_400_al_actualizar_un_caso_de_prueba_con_un_esquema_erróneo(get_url,patch_add_case):
    "Este caso de prueba que si se envía un esquema JSON erróneo en la solicitud de actualización, la API responda con estado HTTP 400, señalando una solicitud mala"
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload={})
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload={},
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_schema_400.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC74_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_nombre_con_mas_de_255_caracteres(get_url,patch_add_case):
    "Este caso de prueba valida que al actualizar el título con más de 255 caracteres, la API retorne estado HTTP 422, indicando que la entidad no es procesable por violación de límites"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=StaticDataCases.title_lange.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")
    assert_response_error_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(raises= "el campo id solo acepta integer pero si se manda un float responde un estado 200 al modificar un caso de prueba : DR-BUG003", run=False)
def test_DR_TC75_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_ID_de_tipo_float(get_url,patch_add_case):
    "Se comprueba que si se usa un ID de tipo float en la URL, la API responda con estado HTTP 422, ya que el ID debe ser entero"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, decimal_number(id_created)),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")
    assert_response_error_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC76_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_con_un_ID_que_no_existe(get_url):
    "Este caso de prueba verifica que al intentar actualizar un caso de prueba con un ID que no existe, la API retorne estado HTTP 404, indicando que el recurso no fue encontrado"
    request = case_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, StaticDataCases.id_does_not_exist.value),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("bad_id",[StaticDataCases.negative_id.value,StaticDataCases.project_does_not_exist.value])
def test_DR_TC77_78_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_con_un_ID_invalido(get_url,bad_id):
    """DR_TC77_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_con_un_ID_de_tipo_negativo
    Se valida que al usar un ID negativo en la URL para actualización, la API responda con estado HTTP 404, ya que IDs negativos no son válidos y no corresponden a recursos existentes
    DR_TC78_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_en_un_proyecto_que_no_existe
    Este caso de prueba comprueba que al intentar actualizar un caso de prueba en un proyecto inexistente, la API retorne estado HTTP 404, indicando que el proyecto no fue encontrado"""
    request = case_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value,bad_id),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC79_Verificar_que_retorna_error_estado_401_al_actualizar_un_caso_de_prueba_con_un_token_invalido(get_url,patch_add_case):
    "Se verifica que al usar un token inválido para la actualización, la API responda con estado HTTP 401, indicando falta de autorización"
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.invalid_token_header.value, payload=json.dumps(request))
    print(response.request.headers.get("Token"))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")
    assert_response_error_token(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("field_",[StaticDataCases.severity_parameter.value,StaticDataCases.priority_parameter.value,StaticDataCases.type_parameter.value,StaticDataCases.status_parameter.value,StaticDataCases.automation_parameter.value])
def test_DR_TC80_81_82_83_84_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_string_en_los_campos(get_url,patch_add_case,field_):
    """DR_TC80_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_severidad_de_tipo_string
    Este caso de prueba valida que al proporcionar un valor de string en lugar de integer para severity, la API retorne estado HTTP 422, rechazando la entidad no procesable.
    DR_TC81_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_prioridad_de_tipo_string
    Este caso de prueba valida que al proporcionar un valor de string en lugar de integer para prioridad, la API retorne estado HTTP 422, rechazando la entidad no procesable.
    DR_TC82_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_string_en_el_campo_tipo
    Este caso de prueba valida que al proporcionar un valor de string en lugar de integer para tipo, la API retorne estado HTTP 422, rechazando la entidad no procesable.
    DR_TC83_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_status_de_tipo_string
    Este caso de prueba valida que al proporcionar un valor de string en lugar de integer para status, la API retorne estado HTTP 422, rechazando la entidad no procesable.
    DR_TC84_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_string_en_el_campo_automatización
    Este caso de prueba valida que al proporcionar un valor de string en lugar de integer para automatización, la API retorne estado HTTP 422, rechazando la entidad no procesable."""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload()
    request[field_] = StaticDataCases.type_string.value
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")
    assert_response_error_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("field",[StaticDataCases.severity_parameter.value,StaticDataCases.priority_parameter.value,StaticDataCases.type_parameter.value,StaticDataCases.status_parameter.value,StaticDataCases.automation_parameter.value])
def test_DR_TC85_86_87_88_89_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_valor_que_no_existe(get_url,patch_add_case,field):
    """DR_TC85_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_severidad_que_no_existe
    Este test verifica que el endpoint maneja correctamente entradas inválidas, retornando un 422 cuando el campo severidad contiene un valor no registrado en el sistema
    DR_TC86_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_prioridad_que_no_existe
    Este test verifica que el endpoint maneja correctamente entradas inválidas, retornando un 422 cuando el campo prioridad contiene un valor no registrado en el sistema
    DR_TC87_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_valor_que_no_existe_en_el_campo_tipo
    Este test verifica que el endpoint maneja correctamente entradas inválidas, retornando un 422 cuando el campo tipo contiene un valor no registrado en el sistema
    DR_TC88_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_status_que_no_existe
    Este test verifica que el endpoint maneja correctamente entradas inválidas, retornando un 422 cuando el campo status contiene un valor no registrado en el sistema
    DR_TC89_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_automatización_que_no_existe
    Este test verifica que el endpoint maneja correctamente entradas inválidas, retornando un 422 cuando el campo automatización contiene un valor no registrado en el sistema"""
    id_created = patch_add_case["result"]["id"]
    request = case_request_payload()
    request[field] = StaticDataCases.value_does_not_exist.value
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                case_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload=request,
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 422)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_422.json")
    assert_response_error_not_empty(response)
