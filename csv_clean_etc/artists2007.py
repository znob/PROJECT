import pandas as pd
import numpy as np
import re
import csv
file = '2007500.csv'
artists = []
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter = ',')
    for row in rd:
        artists.append(row)
new_list = []
for artist in artists:
    dict_toadd = {}
    dict_toadd['Rank'] = artist['Rank']
    artmess= artist['Artist'].title().split('(')
    dict_toadd['Name']= artmess[0].split()
    dict_toadd['TotalSold']=int(re.sub("[^0-9]", "", artist['TotalSold']))
    dict_toadd['MaxPrice']=int(re.sub("[^0-9]", "", artist['MaxPrice']))
    dict_toadd['SaleYear']=2007
    new_list.append(dict_toadd)

clean2007top500 = new_list
