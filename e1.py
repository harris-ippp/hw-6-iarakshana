#!/usr/bin/env python

import requests
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1789/year_to:2016"
resp = requests.get(addr)
from bs4 import BeautifulSoup as bs
html = resp.content
soup = bs(html, "html.parser")
soup.find_all("tr", "election_item")

tr = soup.find_all("tr", "election_item")
#this gives all the election-id tags
trid = []
for tag in soup.find_all('tr', class_ = "election_item") :
    trid.append((tag['id']))
# have to get just the year without string election-id-

#this gives list of all election year rows
tdy = soup.find_all("tr", class_ = "election_item")
y = [x.contents[0] for x in tdy]
#found them both separately but can use for loop to get it as just one


for x in tr:
    tri = (tr['id'][-5:])
    years = tr.find("td").contents[0]
    ELECTION_ID = ('{} {}'.format(years,tri))
    print(ELECTION_ID)
