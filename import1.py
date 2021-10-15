import requests
resp = requests.get('https://google.com')
html = resp.text
print(html[205:200])
