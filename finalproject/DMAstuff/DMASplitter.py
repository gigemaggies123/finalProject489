import pymongo
import collections
from collections import defaultdict
import csv
import re

data = csv.reader(open('CSVs/DMAregions.csv'))
writer = csv.writer(open('SplittedDMARegions.csv', "wb"))

for row in data:
    if row[3][0] == 'D':
        writer.writerow([row[0],row[1],row[2],'State',row[3]])
        continue

    #city = re.match(r'(\w+)(\.-)?( )?(\w+)?( )?(\w+)?( )?(\w+)?', row[2]).group()
    state = re.search('\w+$', row[2]).group()
    
    writer.writerow([row[0],row[1],row[2],state,row[3]])

