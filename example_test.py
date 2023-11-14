# importing the requests library
import requests

# api-endpoint
URL = "http://localhost:8882/"
JSON = {"command": "Browser.Open Browser   http://www.viadee.de    chromium    False"}
response = requests.post(url=URL, json=JSON)

# curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "Browser.Open Browser   https://www.google.de    chromium      False" }'
# curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "Browser.Click    #W0wltc > div" }'
# curl -H "Content-Type: application/json" -X POST http://localhost:8882/ -d '{ "command": "RequestsLibrary.GET    https://www.google.de" }'
# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response data: ", response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Error message: ", response.text)
