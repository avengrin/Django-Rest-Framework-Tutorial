import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint="https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint) # HTTP request
print(get_response.text) # print raw text response
print(get_response.status_code)
# HTTP Request -> HTML
# REST API HTTP Request -> JSON (xml)
# JSON is almost Python Dictionary, bu slightly different
print(get_response.json()['message'])
