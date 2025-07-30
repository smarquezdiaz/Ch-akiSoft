import pytest
import requests

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funtional
def test_SM001_Obtener_todos_los_casos_de_prueba_con_datos_validos(get_url, get_token):
    url = f"{get_url}/suite/DEMO"
    token = get_token

    print(f"URL: {url}")

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200