import requests

url = 'http://127.0.0.1:9000/parse-cmd'
data = [
    {'cmd': 'Generate me phrases about a dinner party'},
    {'cmd': 'Generate me words about a dinner party ontop of a volcano'},
    {'cmd': 'Lets fucking go'},
    {'cmd': 'Translate the phrase I want to go to sleep'},
    {'cmd': 'Create me phrases for running fast'}
]
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

res = requests.post(url, json=data)
print(res.json())
