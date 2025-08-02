
import pytest
from tests.conftest import get_url, get_token
from src.assertions.get_cases_assertions import assert_get_cases_assertion, assert_get_cases_response_schema, assert_response_status_code, assert_entities_field_equal
from src.assertions.post_cases_assertions import assert_post_cases_assertion
from src.assertions.put_cases_assertions import assert_put_cases_assertion
from src.assertions.delete_cases_assertions import assert_delete_cases_assertion

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC01_Verificar_la_obtencion_de_todos_los_casos_de_prueba_de_un_proyecto (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())

@pytest.mark.regression
def test_DR_TC02_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_un_parámetro_que_no_existe (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?esteparametronoexiste=noexiste")
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json())

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC03_Verificar_que_retorna_una_respuesta_401_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_cuando_no_tiene_un_token_valido (get_url):
    response = assert_get_cases_assertion(get_url, "no_token", "DEMO?esteparametronoexiste=noexiste")
    assert_response_status_code(response.status_code, 401)
    assert_get_cases_response_schema(response.json())

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC04_Verificar_que_retorna_una_respuesta_404_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_que_no_existe (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "proyectoquenoexiste")
    assert_response_status_code(response.status_code, 404)
    assert_get_cases_response_schema(response.json())

@pytest.mark.regression
def test_DR_TC05_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_el_método_POST (get_url, get_token):
    response = assert_post_cases_assertion(get_url, get_token, "DEMO")
    assert_response_status_code(response.status_code, 400)
    assert_get_cases_response_schema(response.json())

@pytest.mark.regression
def test_DR_TC06_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_PUT (get_url, get_token):
    response = assert_put_cases_assertion(get_url, get_token, "DEMO")
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json())

@pytest.mark.regression
def test_DR_TC07_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_DELETE (get_url, get_token):
    response = assert_delete_cases_assertion(get_url, get_token, "DEMO")
    assert_response_status_code(response.status_code, 405)
    assert_get_cases_response_schema(response.json())

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC08_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?severity=trivial")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())
    assert_entities_field_equal(response, 6, "severity")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC09_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?priority=low")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())
    assert_entities_field_equal(response, 3, "priority")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC10_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?type=other")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())
    assert_entities_field_equal(response, 1, "type")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC11_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?status=deprecated")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())
    assert_entities_field_equal(response, 2, "status")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC12_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_de_automatizacion (get_url, get_token):
    response = assert_get_cases_assertion(get_url, get_token, "DEMO?automation= is-not-automated")
    assert_response_status_code(response.status_code, 200)
    assert_get_cases_response_schema(response.json())
    assert_entities_field_equal(response, 0, "automation")
