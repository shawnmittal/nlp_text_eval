import requests
import json

url = 'http://127.0.0.1:5000/url_eval'

request_url = 'https://www.cnn.com/2020/08/17/us/coronavirus-college-university/index.html'

j_url = json.dumps(request_url)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_url, headers=headers)
print(r, r.text)