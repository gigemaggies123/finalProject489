import pymongo
import collections
from collections import defaultdict
import csv
import re
import numpy as np
import matplotlib.pyplot as plt

#counties data from www.sqldbpros.com/2011/11/free-zip-code-city-county-state-csv/

countyData = open('CSVs/counties.csv')

counties = csv.reader(countyData)
players = csv.reader(open('heightAndsplit.csv'))

writer1 = csv.writer(open('playersnew.csv', "wb"))
writer2 = csv.writer(open('unwritten.csv', "wb"))

for row in players:
    countyData.seek(0)
    for item in counties:
        if str(row[8]).lower() == str(item[0]).lower() and str(row[9]).lower() == str(item[1]).lower():
            row.append((str(item[2]).title()))
            writer1.writerow(row)
            break
    else:
	writer2.writerow(row)
