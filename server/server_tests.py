import requests

local_url = 'http://127.0.0.1:3000'
prod_url = 'https://langkit-prod.herokuapp.com'
data = [
    {'name': 'Fruit'}
]
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

res = requests.post(prod_url + "/get-topic", json=data).json()

print(res)

