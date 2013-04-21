import pymongo
import collections
from collections import defaultdict
import csv
import re

data = csv.reader(open('fullOutput.csv'))
writer = csv.writer(open('players.csv', "wb"))

for row in data:
    if row[5][0] == 'H':
        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],'City','State',row[9],row[10],row[11],row[12],row[13],row[14]])
        continue
    if row[5][3] != '"':
        inches = (int(row[5][0])*12) + int(10) + (int(row[5][3]))
    else:
        inches = (int(row[5][0])*12) + (int(row[5][2]))

    city = re.match(r'(\w+)(\.)?( )?(\w+)?( )?(\w+)?( )?(\w+)?', row[8]).group()
    state = re.search('\w+$', row[8]).group()
    
    writer.writerow([row[0],row[1],row[2],row[3],row[4],inches,row[6],row[7],city,state,row[9],row[10],row[11],row[12],row[13],row[14]])


