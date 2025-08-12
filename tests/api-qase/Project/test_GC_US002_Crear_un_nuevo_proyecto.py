import pytest
import requests
import jsonschema

import json

from config import TOKEN
from src.assertions.get_cases_assertions import assert_response_status_code
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_project.payloads_project import assert_request_project_payload
from src.resources.payloads.payloads_suite.payloads_suite import assert_request_suite_payload
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_schema_project


def test_SM016_Crear_un_nuevo_conjunto_de_pruebas(get_url, get_token):
    payload = assert_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True

def test_GCTC001_Crear_un_proyecto_exitoso(get_url, get_token):
    payload = assert_request_project_payload()
    assert_response_schema_project(payload, "add_project_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    #assert_response_schema_project(response.json(), "add_project_schema_response.json")
    #assert_response_status_code(response.status_code, 200)
    #assert response.json()["result"]["id"] is not None
    #assert response.json()["status"] == True
    print(response.json())
    print(response.status_code)

#Alta
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC001_Crear_un_proyecto_exitoso2():

   url = "https://api.qase.io/v1/project"
   token = "3b3cae5c58530556817affe99e5de67ec23e811d6ee5f73f4691763471b4cf4c"

   payload_data = {
                     "title": "Prueba20",
                     "code": "prueba20",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")


def test_GCTC002_Verificar_que_de_error_al_enviar_una_URL_mal_formada(get_url, get_token):
    payload = assert_request_project_payload()
    assert_response_schema_project(payload, "add_project_schema_request.json")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.invalid_token_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema_project(response.json(), "post_error404_project_response.json")
    assert_response_status_code(response.status_code, 404)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC002_Verificar_que_de_error_al_enviar_una_URL_mal_formada2():

   url = "https://api.qase.io/v1/poyect"
   token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

   payload_data = {
                     "title": "Prueba13",
                     "code": "prueba13",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
   assert response.status_code == 404

   schema_output = {
           "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "required": [
                    "message"
                ],
                "properties": {
                    "message": {
                        "type": "string"
                    }
                }
   }

   try:
       jsonschema.validate(instance=response.json(), schema=schema_output)
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC003_Verificar_que_de_error_Crear_proyecto_con_nombre_existente_en_lista():

   url = "https://api.qase.io/v1/project"
   token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

   payload_data = {
                     "title": "Prueba20",
                     "code": "prueba20",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
   assert response.status_code == 400

   schema_output = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": [
            "errorFields",
            "errorMessage",
            "status"
        ],
        "properties": {
            "status": {
                "type": "boolean"
            },
            "errorMessage": {
                "type": "string"
            },
            "errorFields": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "error",
                        "field"
                    ],
                    "properties": {
                        "field": {
                            "type": "string"
                        },
                        "error": {
                            "type": "string"
                        }
                    }
                }
            }
        }
   }

   try:
       jsonschema.validate(instance=response.json(), schema=schema_output)
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")

#Media
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC004_Verificar_que_no_permita_crear_un_proyecto_con_un_body_inválido():

   url = "https://api.qase.io/v1/project"
   token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

   payload_data = {
                     "title": "13",
                     "code": "13",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
   assert response.status_code == 400

   schema_output = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "errorFields",
           "errorMessage",
           "status"
       ],
       "properties": {
           "status": {
               "type": "boolean"
           },
           "errorMessage": {
               "type": "string"
           },
           "errorFields": {
               "type": "array",
               "items": {
                   "type": "object",
                   "required": [
                       "error",
                       "field"
                   ],
                   "properties": {
                       "field": {
                           "type": "string"
                       },
                       "error": {
                           "type": "string"
                       }
                   }
               }
           }
       }
   }

   try:
       jsonschema.validate(instance=response.json(), schema=schema_output)
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC005_Verificar_que_no_permita_crear_un_proyecto_con_un_token_incorrecto():

   url = "https://api.qase.io/v1/project"
   token = "af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

   payload_data = {
                     "title": "Prueba21",
                     "code": "prueba21",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
   assert response.status_code == 401

   schema_output = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "error"
       ],
       "properties": {
           "error": {
               "type": "string"
           }
       }
   }

   try:
       jsonschema.validate(instance=response.json(), schema=schema_output)
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC006_Verificar_que_no_permita_crear_un_proyecto_sin_autentificar():

   url = "https://api.qase.io/v1/project"
   token = ""

   payload_data = {
                     "title": "Prueba21",
                     "code": "prueba21",
                     "description": "mmm lolo",
                     "access": "all"
                   }

   schema_input = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "access",
           "code",
           "description",
           "title"
       ],
       "properties": {
           "title": {
               "type": "string"
           },
           "code": {
               "type": "string"
           },
           "description": {
               "type": "string"
           },
           "access": {
               "type": "string"
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
   assert response.status_code == 401

   schema_output = {
       "$schema": "https://json-schema.org/draft/2020-12/schema",
       "type": "object",
       "required": [
           "error"
       ],
       "properties": {
           "error": {
               "type": "string"
           }
       }
   }

   try:
       jsonschema.validate(instance=response.json(), schema=schema_output)
       print("INFO: El payload de entrada es válido según el esquema.")
   except jsonschema.exceptions.ValidationError as err:
       pytest.fail(f"JSON schema dont match [{err}]")

#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC007_Crear_proyecto_con_todos_los_campos_disponibles():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "GrupoProject2",
        "code": "grupopj2",
        "description": "prueba grupo",
        "access": "group",
        "group": "team_group_hash_demo"
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["title", "code", "description", "access", "group"],
        "properties": {
            "title": {"type": "string"},
            "code": {"type": "string"},
            "description": {"type": "string"},
            "access": {"type": "string"},
            "group": {"type": "string"}
        }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload válido según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload NO coincide con esquema: [{err}]")

    payload = json.dumps(payload_data)

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200

    schema_output = {
        "type": "object",
        "required": ["result", "status"],
        "properties": {
            "status": {"type": "boolean"},
            "result": {
                "type": "object",
                "required": ["code"],
                "properties": {
                    "code": {"type": "string"}
                }
            }
        }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: Respuesta válida según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")


#Media
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC008_Verificar_crear_proyecto_sin_description():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "NoDescription2",
        "code": "nodesc2",
        "access": "all"
    }

    schema_input = {
        "type": "object",
        "required": ["title", "code", "access"],
        "properties": {
            "title": {"type": "string"},
            "code": {"type": "string"},
            "access": {"type": "string"}
        }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload válido según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload NO coincide con esquema: [{err}]")

    payload = json.dumps(payload_data)

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200

    schema_output = {
        "type": "object",
        "required": ["result", "status"],
        "properties": {
            "status": {"type": "boolean"},
            "result": {
                "type": "object",
                "required": ["code"],
                "properties": {"code": {"type": "string"}}
            }
        }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: Respuesta válida según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")

#Baja
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC009_Crear_proyecto_con_code_mayusculas():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Prueba22",
        "code": "CODEUPPER2",
        "description": "prueba mayusculas",
        "access": "all"
    }

    schema_input = {
        "type": "object",
        "required": ["title", "code", "description", "access"],
        "properties": {
            "title": {"type": "string"},
            "code": {"type": "string"},
            "description": {"type": "string"},
            "access": {"type": "string"}
        }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload válido según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload NO coincide con esquema: [{err}]")

    payload = json.dumps(payload_data)

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200

    schema_output = {
        "type": "object",
        "required": ["result", "status"],
        "properties": {
            "status": {"type": "boolean"},
            "result": {
                "type": "object",
                "required": ["code"],
                "properties": {"code": {"type": "string"}}
            }
        }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: Respuesta válida según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")

#Alto
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC010_Crear_proyecto_con_code_numerico():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "CodeNum2",
        "code": "1234567",
        "description": "code numérico",
    }

    schema_input = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "required": [
                    "code",
                    "description",
                    "title"
                ],
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "code": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload válido según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload NO coincide con esquema: [{err}]")

    payload = json.dumps(payload_data)

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: Respuesta válida según esquema")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match [{err}]")

#alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC011_Crear_proyecto_sin_title():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "code": "sinTitle",
        "description": "No title",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada cumple con el esquema definido (sin title).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El schema del payload de entrada NO coincide: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: El esquema de salida coincide con la respuesta esperada en error 400.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: JSON schema de salida no coincide: [{err}]")

#Media
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC012_Crear_proyecto_con_code_caracteres_especiales():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Prueba caracteres especiales",
        "code": "inv@lid",
        "description": "codigo invalido",
        "access": "all"
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["title", "code", "description", "access"],
        "properties": {
            "title": {"type": "string"},
            "code": {"type": "string"},
            "description": {"type": "string"},
            "access": {"type": "string"}
        }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada validado correctamente.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR schema entrada: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
                "type": "object",
                "required": [
                    "errorFields",
                    "errorMessage",
                    "status"
                ],
                "properties": {
                    "status": {
                        "type": "boolean"
                    },
                    "errorMessage": {
                        "type": "string"
                    },
                    "errorFields": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "error",
                                "field"
                            ],
                            "properties": {
                                "field": {
                                    "type": "string"
                                },
                                "error": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: Schema de salida coincide para error en caracteres especiales.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR schema salida invalido: [{err}]")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC013_Crear_proyecto_title_1_caracter_valido():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "C",
        "code": "codig2",
        "description": "Proyecto con título de 1 caracter",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido (title 1 caracter).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC014_Crear_proyecto_title_2_caracteres_valido():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "AB",
        "code": "codig3",
        "description": "Proyecto con título de 2 caracteres",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido (title 2 caracteres).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC015_Crear_proyecto_title_224_caracteres_valido():

    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWw",
        "code": "codig224",
        "description": "Título de 224 caracteres válidos",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido (title 224 caracteres).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC016_Crear_proyecto_title_225_caracteres_valido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "AAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWw",
        "code": "coding225",
        "description": "Título de 225 caracteres válidos",

    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido (title 225 caracteres).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")


#Medio
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC017_Crear_proyecto_title_vacio_invalido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "",
        "code": "codvacio1",
        "description": "Título vacío",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada cumple con el esquema definido (sin title).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El schema del payload de entrada NO coincide: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: El esquema de salida coincide con la respuesta esperada en error 400.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: JSON schema de salida no coincide: [{err}]")

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC018_Crear_proyecto_title_256_caracteres_invalido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "AAAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz00112233445566778899AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWw",
        "code": "cod256",
        "description": "Título con 256 caracteres (excede el límite)",

    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada cumple con el esquema definido (sin title).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El schema del payload de entrada NO coincide: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: El esquema de salida coincide con la respuesta esperada en error 400.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: JSON schema de salida no coincide: [{err}]")

#Media
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_GCTC019_Crear_proyecto_code_2_caracteres_valido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Project26",
        "code": "pp",
        "description": "Code de 2 caracteres",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC020_Crear_proyecto_code_5_caracteres_valido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "ProjectCode6",
        "code": "pcodi",
        "description": "Code de 5 caracteres",

    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")

#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC021_Crear_proyecto_code_10_caracteres_valido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Project Code 99",
        "code": "abcdefghik",
        "description": "Code de 10 caracteres",
    }

    schema_input = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description",
                "title"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: Payload de entrada válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Payload inválido: {err}")

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    payload = json.dumps(payload_data)
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
        print("INFO: Payload de salida válido.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Schema salida inválido: {err}")


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC022_Crear_proyecto_code_vacio_invalido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Code vacío2",
        "code": "",
        "description": "Campo 'code' vacío",
    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada cumple con el esquema definido (sin title).")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El schema del payload de entrada NO coincide: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: El esquema de salida coincide con la respuesta esperada en error 400.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: JSON schema de salida no coincide: [{err}]")

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC023_Crear_proyecto_code_15_caracteres_invalido():
    url = "https://api.qase.io/v1/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"

    payload_data = {
        "title": "Code largo2",
        "code": "codigo_muy_largo",
        "description": "Code excede límite de longitud",

    }

    schema_input = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "code",
                "description"
            ],
            "properties": {
                "code": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
    }

    try:
        jsonschema.validate(instance=payload_data, schema=schema_input)
        print("INFO: El payload de entrada cumple con el esquema definido .")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: El schema del payload de entrada NO coincide: [{err}]")

    payload = json.dumps(payload_data)
    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 400

    schema_output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": [
                "errorFields",
                "errorMessage",
                "status"
            ],
            "properties": {
                "status": {
                    "type": "boolean"
                },
                "errorMessage": {
                    "type": "string"
                },
                "errorFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "error",
                            "field"
                        ],
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "error": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
        print("INFO: El esquema de salida coincide con la respuesta esperada en error 400.")
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"ERROR: JSON schema de salida no coincide: [{err}]")