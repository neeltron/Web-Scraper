import requests
from bs4 import BeautifulSoup

url = "https://bbc.com/news"
response = requests.get(url)
print(response.text[:1000])
