import pytest
import requests
import io
from src.headers.headers import get_header_with_token1,get_header_with_invalid_token
from config import BASE_URI,TOKEN
from src.common.logger import log_api_call
from src.assertions.asserts_attachment import assert_response_status_code_global
from src.utils.load_resources import assert_response_schema

@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_DL013_subir_un_archivo_permitido_a_un_proyecto():
    url = f"{BASE_URI}/attachment/DEMO"
    file_content = "Este es un archivo de prueba generado en memoriasdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfdsfsdfsdfsdfsdfdsfsdfsdf"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_up_success_schema_post.json", "schema_attachment")
    assert_response_status_code_global(200, response.status_code)


@pytest.mark.regression
@pytest.mark.negative
def test_DL014_verificar_el_limite_de_tamano_al_momento_de_subir_un_archivo():
    url = f"{BASE_URI}/attachment/DEMO"
    size_in_bytes = 200 * 1024 * 1024
    fake_content = io.BytesIO(b"A" * size_in_bytes)
    files = [('file', ('archivo_grande.txt', fake_content, 'text/plain'))]
    response = requests.post(url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert response.status_code ==413

@pytest.mark.regression
@pytest.mark.negative
def test_DL015_subir_archivo_sin_autenticacion():
    url = f"{BASE_URI}/attachment/DEMO"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_invalid_token(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_invalid_token(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(401, response.status_code)


@pytest.mark.negative
@pytest.mark.regression
def test_DL016_subir_archivo_a_un_proyecto_inexistente():
    url = f"{BASE_URI}/attachment/DEM"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_DL017_subir_archivo_a_un_proyecto_existente_pero_cambiando_de_formato_el_nombre_del_proyecto():
    url = f"{BASE_URI}/attachment/demo"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL018_verificar_el_limite_minimo_de_caracteres_en_el_campo_proyecto():
    url = f"{BASE_URI}/attachment/D"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL019_verificar_el_limite_maximo_de_caracteres_en_el_campo_proyecto():
    url = f"{BASE_URI}/attachment/abcdefghijklmnopqrstuvwxyz"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)


@pytest.mark.negative
@pytest.mark.regression
def test_DL020_enviar_solicitud_de_subida_de_archivo_sin_archivo():
    url = f"{BASE_URI}/attachment/DEMO"
    files = [
    ]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(400, response.status_code)

@pytest.mark.regression
@pytest.mark.negative
def test_DL021_colocar_valores_negativos_en_el_campo_proyecto():
    url = f"{BASE_URI}/attachment/-123"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)

@pytest.mark.negative
@pytest.mark.regression
def test_DL022_colocar_caracteres_especiales_en_el_campo_proyecto():
    url = f"{BASE_URI}/attachment/#"
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachments_Method_Not_Allowed.json", "schema_attachment")
    assert_response_status_code_global(405, response.status_code)


@pytest.mark.negative
@pytest.mark.regression
def test_DL023_colocar_solo_caracter_espacio_en_el_campo_proyecto():
    url = f"{BASE_URI}/attachment/   "
    file_content = "Este es un archivo de prueba generado en memoria"
    file_like = io.BytesIO(file_content.encode('utf-8'))
    files = [('file', ('alle.txt', file_like, 'text/plain'))]
    response = requests.request("POST", url, headers=get_header_with_token1(), files=files)
    log_api_call(method="POST",
                 url=response.url,
                 headers=get_header_with_token1(),
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "attachment_validation_error_schema_post.json", "schema_attachment")
    assert_response_status_code_global(404, response.status_code)