import pytest
import requests
import jsonschema

import json

from src.common.config import URL_SUITE


@pytest.mark.smoke
@pytest.mark.regression
def test_gc_tc001_Crear_un_proyecto_exitoso():

    url = URL_SUITE
    token = a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b

    payload_data = {
        "title": "Suite de Pruebas - Funcionalidades de Pedidos y Entrega",
        "description": "Contiene casos de prueba para el flujo completo de pedidos: desde la selección de productos, checkout, procesamiento de pago, hasta el seguimiento y la entrega por parte del repartidor.",
        "preconditions": "El usuario debe estar logueado y tener una dirección de entrega configurada. Debe haber restaurantes activos y productos disponibles en la zona seleccionada."
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": [
            "result",
            "status"
        ],
        "properties": {
            "status": {
                "type": "boolean"
            },
            "result": {
                "type": "object",
                "required": [
                    "code"
                ],
                "properties": {
                    "code": {
                        "type": "string"
                    }
                }
            }
        }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada es válido según el esquema.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El payload de entrada NO coincide con el esquema esperado: [{err}]")

    payload = json.dumps(payload_data)

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": [
            "result",
            "status"
        ],
        "properties": {
            "status": {
                "type": "boolean"
            },
            "result": {
                "type": "object",
                "required": [
                    "code"
                ],
                "properties": {
                    "code": {
                        "type": "string"
                    }
                }
            }
        }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")