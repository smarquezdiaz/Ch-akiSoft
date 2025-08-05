import pytest
import requests

from config import BASE_URI, TOKEN
from src.assertions.get_project_assertions import assert_get_project_assertion, assert_get_project_response_schema
from src.headers.headers import get_header_with_token

#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_GC001_Obtener_todos_los_proyectos_existentes():
        response = assert_get_project_assertion(BASE_URI, TOKEN, 100, 0)
        assert_get_project_response_schema(response.json(),"get_project_response.json")
        assert response.status_code == 200

#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_GC002_Verificar_que_se_muestre_error_al_mandar_la_URL_mal_formada():
        response = assert_get_project_assertion(BASE_URI + "ss", TOKEN, 100, 0)
        assert_get_project_response_schema(response.json(),"get_error404_project_response.json")
        assert response.status_code == 404

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC003_Obtener_proyectos_con_un_token_incorrecto():
        response = assert_get_project_assertion(BASE_URI, TOKEN + "aa", 100, 0)
        assert_get_project_response_schema(response.json(), "get_error401_proyect_response.json")
        assert response.status_code == 401

#Media
@pytest.mark.funtional
@pytest.mark.regression
def test_GC004_Obtener_un_solo_proyecto_con_limit_1():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 1, 0)
    assert_get_project_response_schema(response.json(), "get_project_response.json")
    assert response.status_code == 200


#media
@pytest.mark.negative
@pytest.mark.regression
def test_GC005_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_limit_con_valor_de_0():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 0, 0)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC006_Verificar_respuesta_de_error_con_limit_como_texto_limit_abc():
    response = assert_get_project_assertion(BASE_URI, TOKEN, "abc", 0)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400

#media
@pytest.mark.negative
@pytest.mark.smoke
def test_GC007_Verificar_que_no_permita_obtener_proyectos_con_limit_5_y_offset_10():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 5, 10)
    assert_get_project_response_schema(response.json(), "get_project_response.json")
    assert response.status_code == 200

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC008_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_negativo():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 10, -5)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC009_Verificar_que_no_permita_obtener_proyectos_con_limit_mayor_al_máximo_limit_101():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 101, 0)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GC010_Verificar_que_no_permita_obtener_proyectos_con_limit_menor_al_limite_inferior():
    response = assert_get_project_assertion(BASE_URI, TOKEN, -1, 0)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400


#Alta
@pytest.mark.xfail(reason="No deberia admitir un offset tan extenso")
@pytest.mark.negative
@pytest.mark.regression
def test_GC011_Verificar_que_no_permita_obtener_la_lista_de_proyectos_con_el_offset_con_valor_excesivo():
    response = assert_get_project_assertion(BASE_URI, TOKEN, 5, 9999999)
    assert_get_project_response_schema(response.json(), "get_error400_project_response.json")
    assert response.status_code == 400

#Alta
@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.regression
def test_GC012_Verificar_que_sin_token_debe_dar_error_sin_autentificaion():
    url = "https://api.qase.io/v1/project?limit=10"
    response = assert_get_project_assertion(BASE_URI, "", 100, 0)
    assert_get_project_response_schema(response.json(), "get_error401_proyect_response.json")
    assert response.status_code == 401



