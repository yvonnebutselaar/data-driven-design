import requests
import json

url = "https://nl.wikipedia.org/api/rest_v1/page/summary/Anime"
req = requests.get(url)
data = json.loads(req.text)

print(data["title"])

for key in data:
    value = data[key]
    print(key, value)