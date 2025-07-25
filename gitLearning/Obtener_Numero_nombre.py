import pytest
import requests

def test_001_verificar_ver_los_datos_de_número_y_nombre_del_departamento_del_museo():
    """Descripción:el usuario debe obtener el número y nombre del departamento del museo"""
    #ambiente
url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
#pasos
#1. seleccionar  Get
#2. click boton send
#3. verificar que se muestre los numeros y nombre departamento
payload = {}
headers = {
  'Cookie': 'incap_ses_1721_1662004=LbIobwzB8CVr/rrgvjjiF6/FgmgAAAAAtf0R/uVbx/Qp8zQ4zaFy0A==; visid_incap_1662004=SESLtp+KT7eSXuEh58Bs4yEjgGgAAAAAQUIPAAAAAADxUZqERhdPttg0U/qAGLwn'
}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
