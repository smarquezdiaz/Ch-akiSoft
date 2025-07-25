import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  'Cookie': 'incap_ses_1721_1662004=LCmEX+kQDQsSen3evjjiFx0ugGgAAAAAVA4TyGVUnxSaIt2mA3Mv5Q==; visid_incap_1662004=SESLtp+KT7eSXuEh58Bs4yEjgGgAAAAAQUIPAAAAAADxUZqERhdPttg0U/qAGLwn'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

