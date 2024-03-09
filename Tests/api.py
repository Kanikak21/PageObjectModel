import requests

url = "https://gorest.co.in/public/v2/users/6697383"

payload = {}
headers = {
  'Authorization': 'Bearer 84c6ac194eb224ce8fdeed89dfd3b4bc5e1a66176a04bcd13cf78f552d0b4b8d'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
