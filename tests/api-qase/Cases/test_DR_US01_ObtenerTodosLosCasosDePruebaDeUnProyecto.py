
import pytest
from src.conftest import get_url, get_token
from src.common.logger import log_api_call
from src.common.static_data_cases import StaticDataCases
from src.assertions.get_cases_assertions import assert_get_cases_assertion, assert_get_cases_response_schema, assert_response_status_code, assert_entities_field_equal, cases_headers, cases_get_url

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC001_Verificar_la_obtencion_de_todos_los_casos_de_prueba_de_un_proyecto (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, "DEMO"), cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(raises= "error si se manda un header que no existe, el sistema devuelve un status 200 : DR-BUG001")
def test_DR_TC002_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_un_parámetro_que_no_existe (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, "DEMO?esteparametronoexiste=noexiste"),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, "DEMO?esteparametronoexiste=noexiste"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
def test_DR_TC003_Verificar_que_retorna_una_respuesta_401_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_cuando_no_tiene_un_token_valido (get_url):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, "DEMO"), cases_headers("invalido"))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers("invalido"),
                 payload=None,
                 token="invalido",
                 response=response
                 )
    assert_response_status_code(response.status_code, 401)
    assert_get_cases_response_schema(response.json(), "cases_schema_401.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
def test_DR_TC004_Verificar_que_retorna_una_respuesta_404_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_que_no_existe (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, "proyectoquenoexiste"), cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, "proyectoquenoexiste"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 404)
    assert_get_cases_response_schema(response.json(), "cases_schema_404.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
def test_DR_TC005_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_el_método_POST (get_url, get_token):
    response = assert_get_cases_assertion("POST", cases_get_url(get_url, "DEMO"), cases_headers(get_token))
    log_api_call(method="POST",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json(), "cases_schema_400.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
def test_DR_TC006_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_PUT (get_url, get_token):
    response = assert_get_cases_assertion("PUT", cases_get_url(get_url, "DEMO"), cases_headers(get_token))
    log_api_call(method="PUT",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.funtional
@pytest.mark.regression
@pytest.mark.negative
def test_DR_TC007_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_DELETE (get_url, get_token):
    response = assert_get_cases_assertion("DELETE", cases_get_url(get_url, "DEMO"), cases_headers(get_token))
    log_api_call(method="DELETE",
                 url=cases_get_url(get_url, "DEMO"),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json(), "cases_schema_405.json")

@pytest.mark.funtional
@pytest.mark.somke
@pytest.mark.regression
def test_DR_TC008_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_critica (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.severity_critical_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.severity_critical_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_critical_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.funtional
@pytest.mark.somke
@pytest.mark.regression
def test_DR_TC009_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_alta (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.priority_high_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.priority_high_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_high_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC010_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_smoke (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.type_smoke_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.type_smoke_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_smoke_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC011_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_actual (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.status_actual_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.status_actual_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_actual_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC012_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_como_automatizacion (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.automation_automated_to_be_automated_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.automation_automated_to_be_automated_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.automation_automated_to_be_automated_value.value, StaticDataCases.automation_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC013_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_mayor (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.severity_major_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.severity_major_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_major_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC014_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_media (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.severity_normal_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.severity_normal_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_normal_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC015_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad_menor (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.severity_minor_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.severity_minor_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.severity_minor_value.value, StaticDataCases.severity_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC016_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_media (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.priority_medium_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.priority_medium_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_medium_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC017_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad_baja (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.priority_low_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.priority_low_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.priority_low_value.value, StaticDataCases.priority_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC018_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_regresion (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.type_regression_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.type_regression_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_regression_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC019_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo_funcional (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.type_functional_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.type_functional_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.type_functional_value.value, StaticDataCases.type_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC020_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_draft (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.status_draft_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.status_draft_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_draft_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC021_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_deprecated (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.status_deprecated_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.status_deprecated_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.status_deprecated_value.value, StaticDataCases.status_parameter.value)

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC022_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_como_no_automatizacion (get_url, get_token):
    response = assert_get_cases_assertion("GET", cases_get_url(get_url, StaticDataCases.automation_is_not_automated_call.value),
                                          cases_headers(get_token))
    log_api_call(method="GET",
                 url=cases_get_url(get_url, StaticDataCases.automation_is_not_automated_call.value),
                 headers=cases_headers(get_token),
                 payload=None,
                 token=get_token,
                 response=response
                 )
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json(),"get_cases_schema_response.json")
    assert_entities_field_equal(response, StaticDataCases.automation_is_not_automated_value.value, StaticDataCases.automation_parameter.value)