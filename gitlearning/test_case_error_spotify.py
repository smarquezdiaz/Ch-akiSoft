import requests
import pytest
# ID US001-01
# Titulo: Obtener el artista con id
# Descripcion: El usuario debe poder obtener obtener un artista con id
# Precondiciones: Ninguna
@pytest.mark.smoke
def test_001_Obtener_un_artista_con_id():
    # Ambiente: URL: https://api.spotify.com/v1/artists/
    url = "https://api.spotify.com/v1/artists/"
    # Pasos
    # 1. Seleccionar GET
    # 2. invocar a la url
    list_url = url + "0TnOYISbd1XYRBk9myaseg"

    response = requests.get(list_url)
    # 3. clic en boton send
    # 4. Verificar estado correcto

    # Resultado esperado
    assert response.status_code == 401

    # Prioridad: High

    # Post condition - Tierdown
    # Ninguna
    # Categoria Smoke