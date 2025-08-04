import pytest
import requests
from config import BASE_URI,TOKEN,TOKEN_Invalido
from src.headers.headers import get_header_with_token,get_header_without_token
from src.resources.payloads.payloads_custom_field.payloads_get_custom_field import get_payload_by_id
from src.assertions.add_custom_field_assertions import assert_post_custom_field_request_schema,assert_post_custom_field_response_schema
from src.common.logger import log_api_call
@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.regression
def test_AE_TC001_crear_campo_personalizado_con_datos_validos():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC001")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc1")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200
    response_data = response.json()
    assert_post_custom_field_response_schema(response_data, "schema_salida_tc1")
@pytest.mark.funcional
@pytest.mark.negativa
@pytest.mark.regression
def test_AE_TC002_Intentar_crear_un_campo_personalizado_sin_titulo():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC002")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc02")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_post_custom_field_response_schema(response.json(), "schema_salida_tc02")


@pytest.mark.funcional
@pytest.mark.negativa
@pytest.mark.regression
def test_AE_TC003_realizar_una_solicitud_sin_autenticacion():
    url = f"{BASE_URI}custom_field"
    headers = get_header_without_token()
    payload = get_payload_by_id("AE_TC003")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN_Invalido,
        response=response
    )
    assert response.status_code == 401
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_authorization")


@pytest.mark.funcional
@pytest.mark.negativa
@pytest.mark.regression
def test_AE_TC004_enviar_valor_no_permitido_en_el_campo_type():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC004")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")


@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.regression
def test_AE_TC005_verificar_campos_obligatorios_title_type_entity_de_campo_personalizado():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC005")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    print("Código de respuesta:", response.status_code)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.regression
def test_AE_TC006_registrar_un_campo_personalizado_con_entity_case():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC006")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")


@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC007_registrar_un_campo_personalizado_con_entity_run():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC007")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC008_registrar_un_campo_personalizado_con_entity_defect():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC008")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC009_validar_que_el_campo_tipo_selectbox_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC009")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
   

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC010_crear_selectbox_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC010")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_post_custom_field_response_schema(response.json(), "schema_salida_especial")

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC011_validar_que_el_campo_tipo_radio_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC011")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC012_crear_radio_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC012")
    assert_post_custom_field_request_schema(payload,"schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_especial")


@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC013_validar_que_el_campo_tipo_multiselec_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC013")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    
@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC014_crear_un_multiselect_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC014")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    


@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC015_enviar_valor_fuera_del_limite_inferior_de_type_numero_negativo():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC015")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    

@pytest.mark.funcional
@pytest.mark.smoke
def test_AE_TC016_Enviar_valor_minimo_permitido_en_type_0():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC016")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")


@pytest.mark.funcional
@pytest.mark.smoke
def test_AE_TC017_Enviar_valor_maximo_permitido_en_type_9():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC017")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 200
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")


@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC018_Enviar_valor_fuera_del_limite_superior_de_type_10():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC018")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")



@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC019_Enviar_numero_decimal_negativo_como_valor_de_type():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC019")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_post_custom_field_response_schema(response.json(), "schema_salida_decimal")


@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC020_Enviar_numero_decimal_positivo_valor_de_type():
    url = f"{BASE_URI}custom_field"
    headers = get_header_with_token()
    payload = get_payload_by_id("AE_TC020")
    response = requests.post(url, headers=headers, json=payload)
    log_api_call(
        method="POST",
        url=url,
        headers=headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert response.status_code == 400
    assert_post_custom_field_response_schema(response.json(), "schema_salida_decimal")
