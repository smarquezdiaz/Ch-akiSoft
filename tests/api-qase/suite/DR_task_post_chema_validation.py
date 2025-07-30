import pytest
import requests
import jsonschema
import json
from config import TOKEN, datos


@pytest.mark.smoke
def test_task_post_chema_validation(datos):
    payload_entrada = {
            "title": "DAVID PRUEBA tarea",
            "description": "esta caso de prueba fue creado desde el codigo",
            "preconditions": "tener el url",
            "postconditions": "borrar despues"
    }

    schema_entrada = {
        "type": "object",
        "required": [
            "description",
            "postconditions",
            "preconditions",
            "title"
        ],
        "properties": {
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "preconditions": {
                "type": "string"
            },
            "postconditions": {
                "type": "string"
            }
        }
    }

    try:
        jsonschema.validate(instance=payload_entrada, schema=schema_entrada)
        print("el payload entrada valida")
    except jsonschema.ValidationError as error:
        pytest.fail(f"el payload de entrada no es igual al payload esperado {error}")

    payload = json.dumps(payload_entrada)

    headers ={
        "Content-Type": "application/json",
        "accept": "application/json",
        "token": TOKEN
    }
    response = requests.post(f"{datos}/case/DEMO", headers=headers, data=payload)

    schema_salida = {
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
                    "id"
                ],
                "properties": {
                    "id": {
                        "type": "integer"
                    }
                }
            }
        }
    }
    try:
        jsonschema.validate(instance=response.json(), schema=schema_salida)
        print("el payload salida valida")
    except jsonschema.ValidationError as error:
        pytest.fail(f"el payloda de salida no es igual al payload esperado {error}")