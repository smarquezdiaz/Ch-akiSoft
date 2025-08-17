import pytest
import requests

from src.assertions.global_assertions import assert_response_schema
from src.headers.headers import get_header_with_token1,get_header_with_invalid_token
from config import BASE_URI,TOKEN
from src.common.logger import log_api_call
from src.assertions.asserts_attachment import assert_response_status_code_global

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_DL001_Obtener_lista_de_archivos_existentes():
    url = f"{BASE_URI}/attachment"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_list_success_schema.json", "schema_attachment")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL002_Obtener_lista_de_archivos_con_un_token_invalido():
    url = f"{BASE_URI}/attachment"
    response = requests.get(url, headers=get_header_with_invalid_token())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_invalid_token(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_error_schema.json", "schema_attachment")
    assert_response_status_code_global(401, response.status_code)

@pytest.mark.positive
@pytest.mark.regression
def test_DL003_Obtener_una_cierta_cantidad_de_archivos():
    url = f"{BASE_URI}/attachment?limit=1&offset=0"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_list_success_schema.json", "schema_attachment")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL004_Verificar_limite_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=1111111&offset=0"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL005_Verificar_limite_negativo_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=-11&offset=0"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL006_Colocar_letras_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=a&offset=0"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al usar el caracter especial # en limit :DL-BUG001 #", run=False)
def test_DL007_Colocar_caracteres_especiales_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment?limit=#&offset=0"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.positive
@pytest.mark.regression
def test_DL008_Omitir_un_archivo():
    url = f"{BASE_URI}/attachment?limit=10&offset=1"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_list_success_schema.json", "schema_attachment")
    assert_response_status_code_global(200, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al exceder el limite de caracteres en offset:DL-BUG002", run=False)
def test_DL009_Verificar_el_limite_en_el_campo_de_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=2312312312313333"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL010_Verificar_limite_negativo_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=-1"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL011_Colocar_letras_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=hola"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.xfail(reason ="error devuelve datos cuando no deberia al usar el caracter especial# en el campo offsetDL-BUG003", run=False)
def test_DL012_Colocar_caracteres_especiales_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment?limit=10&offset=#"
    response = requests.get(url, headers=get_header_with_token1())
    log_api_call(method="GET",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)