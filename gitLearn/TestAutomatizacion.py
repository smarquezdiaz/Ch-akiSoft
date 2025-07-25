
import pytest
import requests


@pytest.mark.smoke
def test_001_Verificar_obtención_de_departamentos_del_Museo_mediante_método_GET():
    # Descripcion: Verificar que el servicio API del museo responde correctamente con la lista de departamentos, incluyendo su ID y nombre, al realizar una solicitud GET a la URL proporcionada.
url = "https://collectionapi.metmuseum.org/public/collection/v1/"
list_url = url + "departments"
response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200