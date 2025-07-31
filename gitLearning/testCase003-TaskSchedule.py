import pytest
import json
import jsonschema
import requests
get_url= "https://api.restful-api.dev/objects"
@pytest.mark.smoke
@pytest.mark.regression

def test_003_agregar_objeto():
    url= get_url

    payload ={
        "name": "Apple  16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    schema_entrada ={
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": [
            "data",
            "name"
        ],
        "properties": {
            "name": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "required": [
                    "CPU model",
                    "Hard disk size",
                    "price",
                    "year"
                ],
                "properties": {
                    "year": {
                        "type": "integer"
                    },
                    "price": {
                        "type": "number"
                    },
                    "CPU model": {
                        "type": "string"
                    },
                    "Hard disk size": {
                        "type": "string"
                    }
                }
            }
        }
    }
    try:
        jsonschema.validate(instance=payload, schema=schema_entrada )

    except jsonschema.exceptions.ValidationError as err:

        pytest.fail(f"JSON schema don't match {err}")
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    schema_salida={
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": [
            "createdAt",
            "data",
            "id",
            "name"
        ],
        "properties": {
            "id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "createdAt": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "required": [
                    "CPU model",
                    "Hard disk size",
                    "price",
                    "year"
                ],
                "properties": {
                    "year": {
                        "type": "integer"
                    },
                    "price": {
                        "type": "number"
                    },
                    "CPU model": {
                        "type": "string"
                    },
                    "Hard disk size": {
                        "type": "string"
                    }
                }
            }
        }
    }
    try:
        jsonschema.validate(instance=response.json(), schema=schema_salida)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200