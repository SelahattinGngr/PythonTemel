import requests
import json
  

result = requests.get("https://www.w3schools.com/")
result = json.loads(result.text)

print(result[0]["title"])
print(type(result))