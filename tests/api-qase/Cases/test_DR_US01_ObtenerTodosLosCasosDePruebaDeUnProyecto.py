import jsonschema
import pytest
import requests
from src.resources.schemas.get_cases_schema_response import schema
from tests.conftest import get_url, get_token

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC01_Verificar_la_obtencion_de_todos_los_casos_de_prueba_de_un_proyecto (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO", headers=headers)
    assert response.status_code == 200, f"no paso la brueba"
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.ValidationError as error:
        pytest.fail(f"el payload de salida no es igual al payload esperado {error}")

@pytest.mark.regression
def test_DR_TC02_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_un_parámetro_que_no_existe (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?esteparametronoexiste=noexiste", headers=headers)
    assert response.status_code == 400, f"no paso la brueba"

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC03_Verificar_que_retorna_una_respuesta_401_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_cuando_no_tiene_un_token_valido (get_url):
    headers = {
        'Token': 'token_invalido',
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO", headers=headers)
    assert response.status_code == 401, f"no paso la brueba"

@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC04_Verificar_que_retorna_una_respuesta_404_al_obtener_todos_los_casos_de_prueba_de_un_proyecto_que_no_existe (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/proyectoquenoexiste", headers=headers)
    assert response.status_code == 404, f"no paso la brueba"

@pytest.mark.regression
def test_DR_TC05_Verificar_que_retorna_una_respuesta_400_al_obtener_todos_los_casos_de_prueba_con_el_método_POST (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.post(f"{get_url}/case/DEMO", headers=headers)
    assert response.status_code == 400, f"no paso la brueba"

@pytest.mark.regression
def test_DR_TC06_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_PUT (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.put(f"{get_url}/case/DEMO", headers=headers)
    assert response.status_code == 405, f"no paso la brueba"

@pytest.mark.regression
def test_DR_TC07_Verificar_que_retorna_una_respuesta_405_al_obtener_todos_los_casos_de_prueba_con_el_método_DELETE (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.delete(f"{get_url}/case/DEMO", headers=headers)
    assert response.status_code == 405, f"no paso la brueba"

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC08_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_severidad (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?severity=trivial", headers=headers)
    assert response.status_code == 200, f"ERROR : {response.status_code}"

    entities = response.json()["result"]["entities"]
    #dependecia a que por lo menos 1 caso de prueba este creado y tenga una severdidad
    assert entities, "No hay casos de prueba registrados"
    for contador in entities:
        if contador["severity"] != 6:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {contador['id']} tiene severity={contador['severity']} "
            )

    print("paso la prueba")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC09_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_prioridad (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?priority=low", headers=headers)
    assert response.status_code == 200, f"ERROR : {response.status_code}"

    entities = response.json()["result"]["entities"]
    # dependecia a que por lo menos 1 caso de prueba este creado y tenga una prioridad
    assert entities, "No hay casos de prueba registrados"
    for contador in entities:
        if contador["priority"] != 3:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {contador['id']} tiene priority={contador['priority']} "
            )

    print("paso la prueba")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC10_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_tipo (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?type=other", headers=headers)
    assert response.status_code == 200, f"ERROR : {response.status_code}"

    entities = response.json()["result"]["entities"]
    # dependecia a que por lo menos 1 caso de prueba este creado y tenga un tipo other
    assert entities, "No hay casos de prueba registrados"
    for contador in entities:
        if contador["type"] != 1:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {contador['id']} tiene type={contador['type']} "
            )

    print("paso la prueba")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC11_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?status=deprecated", headers=headers)
    assert response.status_code == 200, f"ERROR : {response.status_code}"

    entities = response.json()["result"]["entities"]
    # dependecia a que por lo menos 1 caso de prueba este creado y tenga un status seleccionado
    assert entities, "No hay casos de prueba registrados"
    for contador in entities:
        if contador["status"] != 2:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {contador['id']} tiene status={contador['status']} "
            )

    print("paso la prueba")

@pytest.mark.somke
@pytest.mark.funtional
@pytest.mark.regression
def test_DR_TC12_Verificar_la_obtención_de_todos_los_casos_de_prueba_de_un_proyecto_filtrado_por_status_de_automatizacion (get_url, get_token):
    headers = {
        'Token': get_token,
        'accept': 'application/json'
    }
    response = requests.get(f"{get_url}/case/DEMO?automation= is-not-automated", headers=headers)
    assert response.status_code == 200, f"ERROR : {response.status_code}"

    entities = response.json()["result"]["entities"]
    # dependecia a que por lo menos 1 caso de prueba este creado y tenga un status automation
    assert entities, "No hay casos de prueba registrados"
    for contador in entities:
        if contador["automation"] != 0:
            pytest.fail(
                f"Prueba fallada: el caso de prueba {contador['id']} tiene automation={contador['automation']} "
            )

    print("paso la prueba")