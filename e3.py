#!/usr/bin/env python
#was not able to do the loops for all the years and create the df so will do it just with the 2016 read_csv
import pandas as pd
from matplotlib import pyplot as plt

header = pd.read_csv("president_general_2016.csv", nrows = 1).dropna(axis = 1)
d = header.iloc[0].to_dict()

df = pd.read_csv("president_general_2016.csv", index_col = 0,
               thousands = ",", skiprows = [1])

df.rename(inplace = True, columns = d) # rename to democrat/republican
df.dropna(inplace = True, axis = 1)    # drop empty columns
df["Year"] = 2016

#first make a lsit of all the dfs and then make it a pd dataframe 2d list and then concat the columns
df = pd.DataFrame(data = df, columns = ["Democratic", "Republican", "Total Votes Cast", "Year"])
pd.concat(df,#2d list of all the dfs)

#defining republican share
df["Republican Share"] = df["Republican"] / df["Total Votes Cast"]
df.plot(kind = "scatter", x = "Year", y = "Republican Share", alpha =0.2)

#since I have just one year, the plot is just one point for each of the three counties
acc=acc.plot(x='Year', y='Republican Share', kind='bar')
acc.set_xlabel("Years")
acc.set_ylabel("% of Republican Votes")
acc.get_figure().savefig('accomack_county.pdf', format='pdf')
#you would do something similar for the other counties too
albe = df.iloc[2].to_dict()
ale = df.iloc[3].to_dict()
all = df.iloc[4].to_dict()
