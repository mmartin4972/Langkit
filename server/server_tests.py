import requests

local_url = 'http://127.0.0.1:5000'
prod_url = 'https://langkit-prod.herokuapp.com'
url = local_url
data = [
    {'cmd': 'Generate me phrases about a dinner party'},
    {'cmd': 'Generate me words about a dinner party on top of a volcano'},
    {'cmd': 'Generate me phrases about food'},
    {'cmd': 'Translate the phrase I want to go to sleep'},
    {'cmd': 'Create me phrases for running fast'}
]
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

res = requests.post(url + "/parse-cmd", json=data)
print(res.json())

data1 = [
    {"from": "en", "to": "es", "text": "the school is on fire"}
]
res1 = requests.post(url + "/translate", json=data1)
print(res1.json())

data2 = [
    {"prompt": "Generate me phrases about winter"}
]
res2 = requests.post(url + "/naive-gpt3-res", json=data2)
print(res2.json())