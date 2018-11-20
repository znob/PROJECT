import numpy as np
import re
import csv
file = '2013500.csv'
artists = [ ]
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter = ',')
    for row in rd:
        artists.append(row)


new_list = []
for artist in artists:
    dict_toadd = {}
    dict_toadd['Rank']=artist['A']
    name_years=artist['B'].title().split('(')
    dict_toadd['Name'] =  name_years[0].split()
    dict_toadd['TotalSold'] = int(re.sub("[^0-9]", "", artist['C']))
    dict_toadd['TotalLots'] = artist['D']
    dict_toadd['MaxPrice']=int(re.sub("[^0-9]", "", artist['E']))
    dict_toadd['SaleYear']= 2013
    new_list.append(dict_toadd)

clean2013top500 = new_list
