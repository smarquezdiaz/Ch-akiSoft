import pytest
import requests
import json
from config import TOKEN, BASE_URI, TOKEN_Invalido


@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC001_crear_campo_personalizado_con_datos_validos():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "pruebas12",
        "entity": 0,
        "type": 0,
        "placeholder": "12",
        "default_value": "12"
    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)
    response_data = response.json()

    assert response_data["status"] is True
    assert "result" in response_data
    assert "id" in response_data["result"]
    assert isinstance(response_data["result"]["id"], int)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC002_crear_campo_personalizado_con_datos_invalidos():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "funcionalidad1",
        "entity": 10,
        "type": 10
    })
    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC003_realizar_una_solicitud_sin_autenticacion():
    url = f"{BASE_URI}custom_field"
    headers = {
            'Token': TOKEN_Invalido,
            'accept': 'application/json',
            'content-type': 'application/json'
    }
    payload = json.dumps({
            "title": "funcionalidad1",
            "entity": 0,
            "type": 2
    })
    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 401, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC004_enviar_valor_no_permitido_en_el_campo_type():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "funcionalidad1",
        "entity": 1,
        "type": 10
    })
    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC005_verificar_campos_obligatorios_title_type_entity_de_campo_personalizado():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "pruebas13",
        "entity": 0,
        "type": 1
    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC006_registrar_un_campo_personalizado_con_entity_case():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "pruebas14",
        "entity": 0,
        "type": 1
    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)


@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC007_registrar_un_campo_personalizado_con_entity_run():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "pruebas14",
        "entity": 1,
        "type": 1
    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC008_registrar_un_campo_personalizado_con_entity_defect():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
        "title": "pruebas15",
        "entity": 2,
        "type": 1
    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)



@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC009_validar_que_el_campo_tipo_selectbox_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

      "value": [
      {
     "id": 1,
     "title": "prueba 1"
      },
      {
     "id": 2,
      "title": "prueba 2"
      }
      ],
     "title": "ejemploSelectbox",
     "entity": 0,
     "type": 3

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC010_crear_selectbox_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemploSelectbox",
     "entity": 0,
     "type": 3

   })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)



@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC011_validar_que_el_campo_tipo_radio_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

      "value": [
      {
     "id": 1,
     "title": "prueba 1"
      },
      {
     "id": 2,
      "title": "prueba 2"
      }
      ],
     "title": "ejemploradio",
     "entity": 0,
     "type": 3

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC012_crear_radio_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({
     "title": "ejemploradio",
     "entity": 0,
     "type": 5

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.smoke
@pytest.mark.funcional
def test_AE_TC013_validar_que_el_campo_tipo_multiselec_requiere_valores_para_registrar():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

      "value": [
      {
     "id": 1,
     "title": "prueba 1"
      },
      {
     "id": 2,
      "title": "prueba 2"
      }
      ],
     "title": "ejemplomultiselect",
     "entity": 0,
     "type": 6

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC014_Crear_un_multiselect_sin_valores():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemplomultiselect",
     "entity": 0,
     "type": 6

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)


@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC015_Enviar_valor_fuera_del_limite_inferior_de_type_numero_negativo():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemplonegativo",
     "entity": 0,
     "type": -1

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print("Código de respuesta:", response.status_code)


@pytest.mark.funcional
@pytest.mark.smoke
def test_AE_TC016_Enviar_valor_minimo_permitido_en_type_0():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemploMinimoValor",
     "entity": 0,
     "type": 0

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)



@pytest.mark.funcional
@pytest.mark.smoke
def test_AE_TC017_Enviar_valor_maximo_permitido_en_type_9():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemplomaximoValor",
     "entity": 0,
     "type": 9

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 200, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)




@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC018_Enviar_valor_fuera_del_limite_superior_de_type_10():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemploMayorValorPermitido",
     "entity": 0,
     "type": 10

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)


@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC018_Enviar_numero_decimal_negativo_como_valor_de_type():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemploDecimalnegativo",
     "entity": 0,
     "type": -2.5

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)

@pytest.mark.funcional
@pytest.mark.negativa
def test_AE_TC018_Enviar_numero_decimal_positivo_valor_de_type():
    url = f"{BASE_URI}custom_field"
    headers = {
        'Token': TOKEN,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = json.dumps({

     "title": "ejemploDecimalpositivo",
     "entity": 0,
     "type": 3.5

    })

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400, f"Error: status code {response.status_code}, response: {response.text}"
    print(response.text)
    print("Código de respuesta:", response.status_code)