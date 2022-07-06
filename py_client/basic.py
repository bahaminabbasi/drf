import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World"})
print('---------------------------------------------------------------')
# print('headers: ', get_response.headers)
# print('text:' ,get_response.text)
# print(get_response.status_code)
print('json: ',get_response.json())
print('---------------------------------------------------------------')