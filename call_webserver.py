import json
import requests

res = requests.get('http://127.0.0.1:5010')
print(str(res.status_code) + " | " + res.text)