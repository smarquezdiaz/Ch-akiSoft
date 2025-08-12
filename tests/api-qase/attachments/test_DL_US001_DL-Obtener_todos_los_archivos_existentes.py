import pytest
import jsonschema
import requests
from src.assertions.attachments_schema_loader import load_schema
from src.headers.headers import get_header_with_token,get_header_with_token_inv
from config import BASE_URI


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_DL001_Obtener_todos_los_casos_de_prueba():
    url = f"{BASE_URI}/attachment"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 200
    schema = load_schema("attachment_list_success_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.security
@pytest.mark.negative
def test_DL002_Obtener_lista_de_archivos_con_un_token_invalido():
    url = f"{BASE_URI}/attachment"
    response = requests.get(url, headers=get_header_with_token_inv())
    assert response.status_code == 401
    schema = load_schema("attachment_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.functional
@pytest.mark.boundary
@pytest.mark.smoke
def test_DL003_Obtener_una_cierta_cantidad_de_archivos():
    url = f"{BASE_URI}/attachment?limit=1&offset=0"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 200
    schema = load_schema("attachment_list_success_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
def test_DL004_Verificar_limite_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=1111111&offset=0"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)


@pytest.mark.boundary
@pytest.mark.negative
def test_DL005_Verificar_limite_negativo_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=-11&offset=0"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
def test_DL006_Colocar_letras_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=a&offset=0"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al usar el caracter especial #", run=False)
def test_DL007_Colocar_caracteres_especiales_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=#&offset=0"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400 #//error devuelve datos cuando no deberia al usar el caracter especial #
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.functional
@pytest.mark.boundary
@pytest.mark.smoke
def test_DL008_Omitir_un_archivo():
    url = f"{BASE_URI}/attachment?limit=10&offset=1"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 200
    schema = load_schema("attachment_list_success_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al exeder el limite de caracteres en offset", run=False)
def test_DL009_Verificar_el_limite_en_el_campo_de_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=2312312312313333"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400  # //error devuelve datos cuando no deberia al exeder el limite de caracteres en offset
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
def test_DL010_Verificar_limite_negativo_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=-1"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
def test_DL011_Colocar_letras_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=hola"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)

@pytest.mark.boundary
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al usar el caracter especial #", run=False)
def test_DL012_Colocar_caracteres_especiales_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=#"
    response = requests.get(url, headers=get_header_with_token())
    assert response.status_code == 400                  #//error devuelve datos cuando no deberia al usar el caracter especial #
    schema = load_schema("attachment_validation_error_schema")
    jsonschema.validate(instance=response.json(), schema=schema)