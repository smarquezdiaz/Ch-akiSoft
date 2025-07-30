import json
import jsonschema
import pytest
import requests
# ID AE-TC001
# prioridad High

from src.common.config import URL_CUSTOM_FIELD,TOKEN_ADRIAN

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_AE_tC001_Crear_campo_personalizado():
    """Descripcion:El usuario debe poder crear  campos personalizados y este debe mostrar el mensaje 200"""
    # Ambiente
url = URL_CUSTOM_FIELD

headers = {
    'Token': TOKEN_ADRIAN,
    'accept': 'application/json',
    'content-type': 'application/json'
}


payload_data={
    "title": "Tipo de prueba",
    "value": [
        {
            "id": 1,
            "title": "Funcional"
        },
        {
            "id": 2,
            "title": "Smoke"
        },
        {
            "id": 3,
            "title": "Regresion"
        }
    ],
    "entity": 0,
    "type": 3
}

schema_entrada = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": [
        "entity",
        "title",
        "type",
        "value"
    ],
    "properties": {
        "title": {
            "type": "string"
        },
        "value": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "title"
                ]
            }
        },
        "entity": {
            "type": "integer"
        },
        "type": {
            "type": "integer"
        }
    }
}
try:
    jsonschema.validate(instance=payload_data, schema=schema_entrada)
except jsonschema.exceptions.ValidationError as err:
    pytest.fail(f"JSON schema dont match [{err}]")

payload=json.dumps(payload_data)

response = requests.request("POST", url, headers=headers, data=payload)

print("Código de respuesta:", response.status_code)

print(response.text)
assert response.status_code == 200

schema_salida = {
    "title": "Schema de respuesta esperada",
    "type": "object",
    "properties": {
        "status": {"type": "boolean"},
        "result": {
            "type": "object",
            "properties": {
                "id": {"type": "number"}
            },
            "required": ["id"]
        }
    },
    "required": ["status", "result"]
}

try:
    jsonschema.validate(instance=response.json(), schema=schema_salida)
except jsonschema.exceptions.ValidationError as err:
    pytest.fail(f"JSON schema dont match [{err}]")