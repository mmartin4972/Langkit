import requests

local_url = 'http://127.0.0.1:5000'
prod_url = 'https://langkit-prod.herokuapp.com'
url = local_url
data = [
    {'cmd': 'Generate me phrases about a dinner party'}
]
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

res = requests.post(url + "/parse-cmd", json=data)
print(res)
'''
data1 = [
    {"from": "en", "to": "es", "text": "the school is on fire"}
]
res1 = requests.post(url + "/translate", json=data1)
print(res1.json())

data2 = [
    {"prompt": "Generate one word about winter"}
]
res2 = requests.post(url + "/naive-gpt3-res", json=data2)
print(res2.json())

data3 = [{'cmd':'generate me phrases about orange birds', 'to':'es', 'from':'en'}]
res3 = requests.post(url + "/process", json=data3)
print(res3.json())

data4 = [{'cmd':'generate me words about orange birds', 'to':'es', 'from':'en'}]
res4 = requests.post(url + "/process", json=data4)
print(res4.json())

data5 = [{'cmd':'translate the word orange', 'to':'es', 'from':'en'}]
res5 = requests.post(url + "/process", json=data5)
print(res5.json())'''
