import requests

local_url = 'http://127.0.0.1:3000'
prod_url = 'https://langkit-prod.herokuapp.com'
data = [
    {'cmd': 'Generate me phrases about a dinner party'},
    {'cmd': 'Generate me words about a dinner party on top of a volcano'},
    {'cmd': 'Generate me phrases about food'},
    {'cmd': 'Translate the phrase I want to go to sleep'},
    {'cmd': 'Create me phrases for running fast'}
]
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

res = requests.post(prod_url + "/parse-cmd", json=data).json()
print(res)

data1 = [
    {"from": "en", "to": "es", "text": "the school is on fire"}
]
res1 = requests.post(prod_url + "/translate", json=data1).json()
print(res1[0])

