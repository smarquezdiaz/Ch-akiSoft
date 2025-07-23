import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
