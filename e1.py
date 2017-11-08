#!/usr/bin/env python

import requests
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1789/year_to:2016"
resp = requests.get(addr)
s = resp.status_code
t = resp.text
j = resp.json()
from bs4 import BeautifulSoup as bs
html = resp.content
soup = bs(html, "html.parser")
soup.find_all("tr", "election_item")

for tag in soup.find_all(class_ = "election_item"):
    print(tag.get('id'))
