

import pytest
import requests
import json


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM002_Crear_un_nuevo_conjunto_de_pruebas(get_url, get_token):
    url = f"{get_url}/suite/DEMO"
    token = get_token

    payload = json.dumps({
        "title": "Suite de Pruebas - Funcionalidades de Pedidos y Entrega",
        "description": "Contiene casos de prueba para el flujo completo de pedidos: desde la selección de productos, checkout, procesamiento de pago, hasta el seguimiento y la entrega por parte del repartidor.",
        "preconditions": "El usuario debe estar logueado y tener una dirección de entrega configurada. Debe haber restaurantes activos y productos disponibles en la zona seleccionada."
    })

    headers = {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload) # Validar verbo
    assert response.status_code == 200 # Validar codigo
    #validar schema
