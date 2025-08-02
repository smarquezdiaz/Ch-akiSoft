import pytest
import json
import jsonschema
import requests

from config import BASE_URI,TOKEN
def get_headers(token=TOKEN, content_type=False):
    headers = {
        'accept': 'application/json',
        'Token': token
    }
    if content_type:
        headers['Content-Type'] = 'application/json'
    return headers
def get_headers2(token=TOKEN, content_type=False):
    headers = {
        'accept': 'application/json',
        'Token': token,
        'Content-Type': 'application/json'
    }
    if content_type:
        headers['Content-Type'] = 'application/json'
    return headers

@pytest.mark.smoke
@pytest.mark.regression

def test_SM001_Obtener_todos_los_casos_de_prueba():

    url = f"{BASE_URI}/attachment"
    attachment_response_schema = {
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
                    "count",
                    "entities",
                    "filtered",
                    "total"
                ],
                "properties": {
                    "total": {
                        "type": "integer"
                    },
                    "filtered": {
                        "type": "integer"
                    },
                    "count": {
                        "type": "integer"
                    },
                    "entities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "extension",
                                "file",
                                "full_path",
                                "hash",
                                "mime",
                                "size"
                            ],
                            "properties": {
                                "hash": {
                                    "type": "string"
                                },
                                "file": {
                                    "type": "string"
                                },
                                "mime": {
                                    "type": "string"
                                },
                                "size": {
                                    "type": "integer"
                                },
                                "extension": {
                                    "type": "string"
                                },
                                "full_path": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    response = requests.get(url, headers =get_headers())
    assert response.status_code == 200
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM002_Obtener_lista_de_archivos_con_un_token_invalido():
    url = "https://api.qase.io/v1/attachment"
    invalid_token = "0676837bed7d0effa596f6b154877cccea3008d2cd807a30d503dedd057b513z"
    attachment_response_schema ={
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

    response = requests.get(url, headers=get_headers(token=invalid_token))
    assert response.status_code == 401
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM003_Obtener_una_cierta_cantidad_de_archivos():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "limit": 1
    })
    attachment_response_schema = {
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
                    "count",
                    "entities",
                    "filtered",
                    "total"
                ],
                "properties": {
                    "total": {
                        "type": "integer"
                    },
                    "filtered": {
                        "type": "integer"
                    },
                    "count": {
                        "type": "integer"
                    },
                    "entities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "extension",
                                "file",
                                "full_path",
                                "hash",
                                "mime",
                                "size"
                            ],
                            "properties": {
                                "hash": {
                                    "type": "string"
                                },
                                "file": {
                                    "type": "string"
                                },
                                "mime": {
                                    "type": "string"
                                },
                                "size": {
                                    "type": "integer"
                                },
                                "extension": {
                                    "type": "string"
                                },
                                "full_path": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 200
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM004_Verificar_limite_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "limit": 1111111
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM005_Verificar_limite_negativo_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "limit": -11
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM006_Colocar_letras_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "limit": "a"
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM007_Colocar_caracteres_especiales_en_el_campo_conjunto_de_resultados():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "limit": "·$%!"
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM008_Omitir_un_archivo():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "offset": 1
    })
    attachment_response_schema = {
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
                "count",
                "entities",
                "filtered",
                "total"
            ],
            "properties": {
                "total": {
                    "type": "integer"
                },
                "filtered": {
                    "type": "integer"
                },
                "count": {
                    "type": "integer"
                },
                "entities": {
                    "type": "array"
                }
            }
        }
    }
}
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 200
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM009_Verificar_el_limite_en_el_campo_de_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "offset": 2312312312313333
    })
    attachment_response_schema = {
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
                "count",
                "entities",
                "filtered",
                "total"
            ],
            "properties": {
                "total": {
                    "type": "integer"
                },
                "filtered": {
                    "type": "integer"
                },
                "count": {
                    "type": "integer"
                },
                "entities": {
                    "type": "array"
                }
            }
        }
    }
}
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 200
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM010_Verificar_limite_negativo_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "offset": -1
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM011_Colocar_letras_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "offset": "hola"
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)

def test_SM012_Colocar_caracteres_especiales_en_el_campo_omitir_entidades():
    url = f"{BASE_URI}/attachment"
    payload = json.dumps({
        "offset": "·$ª()"
    })
    attachment_response_schema = {
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
    response = requests.get(url, headers=get_headers2(), data=payload)
    assert response.status_code == 400
    response_json = response.json()
    jsonschema.validate(instance=response_json, schema=attachment_response_schema)
