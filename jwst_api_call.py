import requests

url = "https://api.jwstapi.com/all/type/jpg"

payload={}
headers = {
  'X-API-KEY': 'b2343446-6ef5-4485-a3cc-f46b2c7e8106'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
