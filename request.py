import requests

url = 'http://127.0.0.1:5000/'
r = requests.post(url,json={'Age':20, 'Sex':9, 'Smoker':6})

print(r.json())