import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.caverbob.com/usalong.htm"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("table")
elements = results.find_all("tr")

caves = []
for element in elements:
  row = []
  for cell in soup.find_all("td"):
    row.append(cell.text)
    cell.next_sibling
  caves.append(row)


with open('raw.json', 'w') as f:
    json.dump(caves, f)