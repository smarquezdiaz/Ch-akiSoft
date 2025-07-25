import requests
import pytest
# ID US001-01
# Titulo: Obtener el objeto con id 1000
# Descripcion: El usuario debe poder obtener obtener un objeto con id 1000
# Precondiciones: Ninguna
@pytest.mark.smoke
def test_001_Obtener_un_objeto_con_id_1000():
    # Ambiente: URL: https://api.restful-api.dev/
    url = "https://api.restful-api.dev/"
    # Pasos
    # 1. Seleccionar GET
    # 2. invocar a la url
    list_url = url + "objects/1000"

    response = requests.get(list_url)
    # 3. clic en boton send
    # 4. Verificar estado correcto

    # Resultado esperado
    assert response.status_code == 404

    # Prioridad: High

    # Post condition - Tierdown
    # Ninguna
    # Categoria Smoke