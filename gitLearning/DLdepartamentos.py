import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  'Cookie': 'incap_ses_1722_1662004=HDrKTuHpDVkaa2yFPcblF0rHgmgAAAAAkrKfne4O02cYinIFo9GeDw==; visid_incap_1662004=wZXoFaxIRw+X8vSGgDPE2zQjgGgAAAAAQUIPAAAAAADVmKDbGkTljb/XWLI/pG7c'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)