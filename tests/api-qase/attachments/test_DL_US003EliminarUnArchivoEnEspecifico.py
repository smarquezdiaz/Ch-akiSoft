import pytest
import requests
from config import BASE_URI, TOKEN
from src.headers.headers import get_header_with_token1, get_header_with_invalid_token
from src.common.logger import log_api_call
from src.assertions.asserts_attachment import assert_response_status_code_global
from src.utils.load_resources import assert_response_schema
from src.utils.getHash import obtener_hash_archivo
from src.utils.attachment_utils_request import delete_request, get_request, build_attachment_url, build_invalid_url
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
#Descripcion: elimina un archivo mediante un hash unico
#Prioridad: Alta
def test_DL024_eliminar_archivo_por_hash_valido():
    hash_archivo = obtener_hash_archivo(
        file_name="archivo_eliminar.txt",
        file_content="Contenido temporal para eliminar"
    )
    url = build_attachment_url(hash_archivo)
    response = delete_request(url, headers=get_header_with_token1())
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "attachment_delete_200.json", "schema_attachment")

    # GET para validar que fue eliminado
    response_get = get_request(build_attachment_url(hash_archivo), headers=get_header_with_token1())
    assert_response_status_code_global(404, response_get.status_code)
#Descripcion: Devuelve un error 405 al tratar de elimar un archivo sin agregarle un hash
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC025_eliminar_archivo_sin_hash():
    response = delete_request(build_attachment_url(""), headers=get_header_with_token1())
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(405, response.status_code)
    assert_response_schema(response.json(), "attachment_error_405.json", "schema_attachment")

#Descripcion: Devuelve un error 404 al tratar de eliminar mediante un hash inexistente
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC026_eliminar_archivo_inexistente():
    response = delete_request(build_attachment_url("abc123def456ghi789"), headers=get_header_with_token1())
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(404, response.status_code)
    assert_response_schema(response.json(), "attachment_error_404.json", "schema_attachment")

#Descripcion: Debuelve un error 401 al tratar de eliminar un archivo si un token
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC027_eliminar_archivo_sin_token():
    response = delete_request(build_attachment_url("abc123def456ghi789"), headers={})
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(401, response.status_code)
    assert_response_schema(response.json(), "attachment_error_401.json", "schema_attachment")

#Descripcion: Debuelve un error 401 al tratar de eliminar un archivo con un token invalido
#Prioridad:  Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC028_eliminar_archivo_con_token_invalido():
    response = delete_request(
        build_attachment_url("abc123def456ghi789"),
        headers=get_header_with_invalid_token(),
        token_override="INVALID_TOKEN"
    )
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(401, response.status_code)
    assert_response_schema(response.json(), "attachment_error_401.json", "schema_attachment")

#Descripcion: Debuelve un error 404 al tratar de colocar caracteres especiales, numericos y valores negativos en el campo hashs
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("hash_value", [
    "!@#$%^&*()_+=?", "-123456", "1234567890"
])
def test_DL_TC029_030_032_hash_invalidos(hash_value):
    response = delete_request(build_attachment_url(hash_value), headers=get_header_with_token1())
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(404, response.status_code)
    assert_response_schema(response.json(), "attachment_error_404.json", "schema_attachment")

#Descripcion: Debuelve un error 404 al tratar de colocar el caracter espacio "  " en el campo hashs
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC031_Colocar_solo_carácter_espacio_en_el_campo_hash():
    hash_espacio = " "
    url = f"{BASE_URI}/attachment/{hash_espacio}"
    response = requests.delete(url, headers=get_header_with_token1())
    log_api_call("DELETE", url, get_header_with_token1(), None, TOKEN, response)
    assert_response_status_code_global(404, response.status_code)
    assert_response_schema(response.json(), "attachment_error_404.json", "schema_attachment")
