#!/usr/bin/env python
#was not able to create the ELECTION_ID file required for part 2 and 3 so will just write method
#for what I can do without the file
import requests
for line in open("ELECTION_ID"):
    requests.get("http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/")
    #{} is each year's election id from part 1 so we can get all the csv files required
    
