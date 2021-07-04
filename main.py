import requests

url = "https://bbc.com/news"
response = requests.get(url)
print(response.text[:1000])
