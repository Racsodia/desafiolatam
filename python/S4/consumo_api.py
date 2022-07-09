import requests

url = "https://jsonplaceholder.typicode.com/posts"
api_key="wmDoTAJLPVThCo8asBkARRtcb9ECEv15sUjPTmPN"

payload={"api_key": api_key}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)