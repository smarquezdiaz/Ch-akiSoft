import pytest
import requests
import jsonschema

import json

@pytest.mark.smoke
@pytest.mark.regression
def test_001_obtener_la_lista_de_objetos_del_sistema(get_url):
    """Descripcion: El usuario debe obtener la lista completa de todos los objetos existentes en el sistema"""
    url = get_url + "objects"
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.regression
def test_001_Obtener_la_lista_de_objetos_del_sistema():
    """Descripcion: El usuario debe obtener la lista completa de todos los objetos existentes en el sistema"""
    list_url = "https://api.restful-api.dev/"
    response = requests.get(list_url + "objects")
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.regression
def test_002_adicionar_objeto(get_url):
    """Descripcion: El usuario desea adicionar un objeto a la lista"""
    url = get_url + "objects"
    payload = json.dumps({
        "name": "Apple Diplo",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200

    schema = {
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
            "data": {  # Este es el esquema para el campo 'data' dentro de la respuesta
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
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")

@pytest.mark.smoke
@pytest.mark.regression
def test_003_modificar_objeto(get_url, add_object):
    ... # Aquí iría el código para modificar un objeto