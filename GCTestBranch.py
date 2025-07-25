import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.158", "Google Chrome";v="138.0.7204.158"',
  'sec-ch-ua-platform': '"Windows"',
  'Referer': 'https://www.youtube.com/',
  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-form-factors': '"Desktop"',
  'sec-ch-ua-wow64': '?0',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-full-version': '"138.0.7204.158"',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'Cookie': 'incap_ses_624_1662004=EukcHhTDh3VDj+La8uSoCCNtgWgAAAAAtNz6KHub1k0YYDYA4TsXsg==; visid_incap_1662004=VuGrvFLSQMirN4f4PQcF/SskgGgAAAAAQUIPAAAAAACLzR1LGkLsZyKc4KL3Cmvi'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)