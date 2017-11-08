#!/usr/bin/env python

import requests
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1789/year_to:2016"
resp = requests.get(addr)
from bs4 import BeautifulSoup as bs
html = resp.content
soup = bs(html, "html.parser")
soup.find_all("tr", "election_item")

#this gives all the election-id tags
trid = []
for tag in soup.find_all('tr', class_ = "election_item") :
    trid.append((tag['id']))
# have to get just the year without string election-id-

#this gives list of all election year rows
tdy = soup.find_all("tr", class_ = "election_item")
y = [x.contents[0] for x in tdy]

id = trid.find("td").contents[0]
print(id)

# have to get just the year without the extra information
#not sure how to get two lists in correct format so will just write method
#have left in the different commands I tried

print(trid.contents[0])

l = [x.contents for x in soup.find_all"tr")[1:]]

>>> for tdi in tdy:
...     row = ''
...     rows = tdi.find_all('tr')
...     for row in rows:
...             if(row.text.find("td"):
>>>                    print(row.text))
>>>

trid.merge(tdy)
#have to then join the two lists together using join command)

#after getting both lists, you would join them to make one text file in election id and format it as a column list
ELECTION_ID = '\n'.join('{} {}'.format(x[0],x[1])
