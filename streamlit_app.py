import requests
from bs4 import BeautifulSoup

url = "https://arturmargaryann.github.io/SchoolDesk/"

response = requests.get(url)
response.encoding = "utf-8"

html = response.text

soup = BeautifulSoup(html, "html.parser")
pretty_html = soup.prettify()

print(pretty_html)
