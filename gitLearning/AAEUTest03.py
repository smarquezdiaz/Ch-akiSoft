import pytest
import requests
import json
@pytest.mark.smoke
#id AAEU-03
#prioridad media
def test_03_error400 ():
    """Descripción:nos debe mostrar el error 400 al crear un equipo con la falta de un dato  """
# ambiente
url = "https://api.restful-api.dev/objects"
#paso 1 añadir  un equipo nuevo que le falte el dato name
#paso 2   añadir los siguientes payloads y headers
payload = "{ \"name\": , \"data\": { \"year\": 2019, \"price\": 1849.99, \"CPU model\": \"Intel Core i9\", \"Hard disk size\": \"1 TB\" } }\r\n"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
# verificar que se muestre el error 400 por añadir  un equipo  que le falte un nombre
assert response.status_code == 400
print(response.text)
