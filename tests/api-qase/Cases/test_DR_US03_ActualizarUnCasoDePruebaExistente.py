
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
from src.resources.payloads.payloads_case.payloads_post_case import assert_request_payload, name_random_cases, random_severity_case, random_status_case, random_type_case, random_priority_case, random_automation_case, decimal_number
from src.common.url import assert_patch_join

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC54_Verificar_que_se_retorna_estado_200_al_actualizar_solo_un_campo_title_de_un_caso_de_prueba_Smoke(get_url,patch_add_case):
    id_created=patch_add_case["result"]["id"]
    request=assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value,id_created),
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
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(name_random_cases(), random_severity_case(), random_priority_case(),
                                     random_type_case(), random_status_case(), random_automation_case())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC56_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_crítico_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.severity_critical_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC57_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_mayor_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.severity_major_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC58_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_normal_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.severity_normal_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC59_Verificar_que_la_actualización_del_campo_severidad_de_un_caso_de_prueba_a_menor_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.severity_minor_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC60_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_medio_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(priority=StaticDataCases.priority_medium_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC61_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_bajo_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(priority=StaticDataCases.priority_low_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC62_Verificar_que_la_actualización_del_campo_prioridad_de_un_caso_de_prueba_a_alto_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(priority=StaticDataCases.priority_high_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC63_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_regresión_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(type_=StaticDataCases.type_regression_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC64_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_funcional_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(type_=StaticDataCases.type_functional_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC65_Verificar_que_la_actualización_del_campo_tipo_de_un_caso_de_prueba_a_smoke_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(type_=StaticDataCases.type_smoke_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC66_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_draft_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(status=StaticDataCases.status_draft_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC67_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_deprecated_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(status=StaticDataCases.status_deprecated_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC68_Verificar_que_la_actualización_del_campo_status_de_un_caso_de_prueba_a_actual_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(status=StaticDataCases.status_draft_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=StaticDataCases.title_one.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC70_Verificar_que_la_actualización_del_campo_automatización_de_un_caso_de_prueba_a_no_automatización_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(automation=StaticDataCases.automation_is_not_automated_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC71_Verificar_que_la_actualización_del_campo_automatización_de_un_caso_de_prueba_a_automatización_retorne_un_estado_200(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(automation=StaticDataCases.automation_automated_to_be_automated_value.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=StaticDataCases.empty_title.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
    id_created = patch_add_case["result"]["id"]
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
                                header_type=StaticDataHeaders.default_header.value, payload={})
    log_api_call(method=StaticDataVerbs.patch.value,
                 url=response.url,
                 headers=response.headers,
                 payload={},
                 token=response.request.headers.get("Token"),
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_post_schema_400.json")
    assert_response_error_status_not_empty(response)

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC74_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_nombre_con_mas_de_255_caracteres(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=StaticDataCases.title_lange.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC75_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_ID_de_tipo_float(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, decimal_number(id_created)),
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
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, StaticDataCases.id_does_not_exist.value),
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
def test_DR_TC77_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_con_un_ID_de_tipo_negativo(get_url):
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value,
                                                  StaticDataCases.negative_id.value),
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
def test_DR_TC78_Verificar_que_retorna_error_estado_404_al_actualizar_un_caso_de_prueba_en_un_proyecto_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataCases.project_does_not_exist.value, id_created),
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
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(title=name_random_cases())
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC80_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_severidad_de_tipo_string(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.type_string.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC81_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_prioridad_de_tipo_string(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(priority=StaticDataCases.type_string.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC82_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_string_en_el_campo_tipo(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(type_=StaticDataCases.type_string.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC83_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_status_de_tipo_string(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(status=StaticDataCases.type_string.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC84_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_string_en_el_campo_automatización(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(automation=StaticDataCases.type_string.value)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC85_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_severidad_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(severity=StaticDataCases.value_does_not_exist.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC86_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_prioridad_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(priority=StaticDataCases.value_does_not_exist.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC87_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_valor_que_no_existe_en_el_campo_tipo(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(type_=StaticDataCases.value_does_not_exist.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC88_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_un_status_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(status=StaticDataCases.value_does_not_exist.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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
def test_DR_TC89_Verificar_que_retorna_error_estado_422_al_actualizar_un_caso_de_prueba_con_una_automatización_que_no_existe(get_url,patch_add_case):
    id_created = patch_add_case["result"]["id"]
    request = assert_request_payload(automation=StaticDataCases.value_does_not_exist.value)
    assert_get_cases_response_schema(request, "patch_cases_schema_request.json")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,
                                assert_patch_join(StaticDataSuites.default_url_suffix.value, id_created),
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