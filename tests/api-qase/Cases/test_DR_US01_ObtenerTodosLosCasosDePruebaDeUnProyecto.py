
import pytest
from tests.conftest import get_url, get_token
from src.common.logger import log_api_call
from src.common.static_data_cases import StaticDataCases
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.common.url import get_url_parametrized
from src.headers.headers import get_header_with_token, get_header_with_invalid_token
from src.utils.api_calls import request_function
from src.assertions.get_cases_assertions import assert_get_cases_response_schema, assert_entities_field_equal, assert_response_status_code_case

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC001_Verificar_la_obtencion_de_todos_los_casos_de_prueba_de_un_proyecto (get_url,get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value, header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(raises= "error si se manda un header que no existe, el sistema devuelve un status 200 : DR-BUG001")
def test_DR_TC002_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_un_parámetro_que_no_existe (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, "/DEMO?esteparametronoexiste=noexiste", header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, "/DEMO?esteparametronoexiste=noexiste"),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 400)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC003_Verificar_que_retorna_una_respuesta_401_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_cuando_no_tiene_un_token_valido (get_url):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value, header_type=StaticDataHeaders.invalid_token_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_invalid_token(),
                 payload=None,
                 token= get_header_with_invalid_token()["Token"],
                 response=response
                 )
    print (response.status_code)
    assert_response_status_code_case(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC004_Verificar_que_retorna_una_respuesta_404_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_que_no_existe (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, "/proyectoquenoexiste", header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, "/proyectoquenoexiste"),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC005_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_el_método_POST (get_url, get_token):
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value, header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.post.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_schema_400.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC006_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_PUT (get_url, get_token):
    response = request_function(StaticDataVerbs.put.value, get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value, header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.put.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.negative
@pytest.mark.regression
def test_DR_TC007_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_DELETE (get_url, get_token):
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value, header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataSuites.default_url_suffix.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC008_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_critica (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.severity_critical_call.value, header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.severity_critical_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_critical_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC009_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_alta (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.priority_high_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.priority_high_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_high_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC010_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_smoke (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.type_smoke_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.type_smoke_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_smoke_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC011_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_actual (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.status_actual_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.status_actual_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_actual_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC012_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_como_automatizacion (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.automation_automated_to_be_automated_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.automation_automated_to_be_automated_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.automation_automated_to_be_automated_value.value, StaticDataCases.automation_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC013_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_mayor (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.severity_major_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataCases.severity_major_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_major_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC014_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_media (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.severity_normal_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.severity_normal_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_normal_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC015_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_menor (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.severity_minor_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.severity_minor_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_minor_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC016_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_media (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.priority_medium_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.priority_medium_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_medium_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC017_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_baja (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.priority_low_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.priority_low_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_low_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC018_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_regresion (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.type_regression_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.type_regression_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_regression_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC019_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_funcional (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.type_functional_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.type_functional_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_functional_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC020_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_draft (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.status_draft_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.status_draft_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_draft_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC021_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_deprecated (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.status_deprecated_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value,StaticDataCases.status_deprecated_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_deprecated_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC022_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_como_no_automatizacion (get_url, get_token):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.case.value, code=StaticDataCases.automation_is_not_automated_call.value,
                                header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.get.value,
                 url=get_url_parametrized(get_url, StaticDataModules.case.value, StaticDataCases.automation_is_not_automated_call.value),
                 headers=get_header_with_token(),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code_case(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.automation_is_not_automated_value.value, StaticDataCases.automation_parameter.value)