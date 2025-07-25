import requests
import json

url = "https://api.todoist.com/api/v1/sections"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 636d85f1f3f0fe9ba6a2dfcba0d580f58469c7c2',
  'Cookie': 'tduser=v4.public.eyJ1c2VyX2lkIjogNDQwOTAxMDUsICJleHAiOiAiMjAyNS0wOC0wNVQyMjo1NjowMCswMDowMCJ9ZIiSncQH2aaD-OywQY4t6ItBtOLO8c_Nc9cu0xYESaM5mFh8cvEaMGni9TEnIsKZhDj9h7I1zZ2zL-HNlvkuAQ; todoistd="/CUdA09psYiwY7pwgn9sRGC/RQQ=?"; csrf=f6c18d0a95f5432cb2979945a37c4a11'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
