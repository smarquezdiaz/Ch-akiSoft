from urllib.request import URLopener
import pytest
import requests

#Prioridad
#Medium

@pytest.mark.smoke
def test_001_Verificar_que_se_muestre_los_departamentos_existentes():
     """Descripcion: El usuario obtiene una lista de los departamentos del museo."""

     #Ambiente

     url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

     # Pasos:
     # 1. Abrir Postman.
     # 2. Seleccionar metodo get
     # 3. Ingresar la URL: https://collectionapi.metmuseum.org/public/collection/v1/departments.

     list_url = url + "/departments"

     # 4. Enviar la solicitud.

     response = requests.get(list_url)

