#!/usr/bin/env python
#was not able to this for part 2 and 3 so will just write method
#for what I can do
import requests
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1789/year_to:2016"
resp = requests.get(addr)
from bs4 import BeautifulSoup as bs
html = resp.content
soup = bs(html, "html.parser")
tr = soup.find_all("tr", "election_item")

#to get list of years
year = []
for t in tr:
    year.append(t.contents[1].text)

for line in open("ELECTION_ID"):
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"


    #{} is each year's election id from part 1 so we can get all the csv files required
