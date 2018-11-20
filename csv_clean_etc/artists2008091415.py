#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re


# In[7]:


file = 'topartistsoverall2016.csv'


# In[11]:


import csv
def get_data(file):
    file = file
    artists = []
    with open(file) as fh:
        rd = csv.DictReader(fh, delimiter = ',')
        for row in rd:
            artists.append(row)
    return artists


# In[15]:


x = get_data(file)
x[:2]


# In[14]:


titles2015 = ['Rank', 'Artist', 'Turnover', 'Sold lots', 'Top Auction Result']


# In[43]:


def clean_data(read_file, year):
    return_list = []
    for artist in read_file:
        new_item = {}
        new_item['Rank'] = int(artist['A'])
        name_date = artist['B'].title().split('(')
        new_item['Name'] = name_date[0].split()
        years = name_date[-1].strip('()').split('-')
        new_item['Life'] = years
        new_item['TotalSold'] = int(re.sub("[^0-9]", "", artist['C']))
        new_item['TotalLots'] = int(re.sub("[^0-9]", "", artist['D']))
        new_item['MaxPrice'] = int(re.sub("[^0-9]", "", artist['E']))
        new_item['SaleYear'] = year
        return_list.append(new_item)
    return return_list


# In[44]:


clean2015top500 = clean_data(x, 2015)


file1 = '2014top500.csv'
y = get_data(file1)
clean2014top500 = clean_data(y, 2014)


file2 = '2009500.csv'
z = get_data(file2)


def clean_data_extended(read_file, year):
    return_list = []
    for artist in read_file:
        new_item = {}
        new_item['Rank'] = int(artist['A'])
        name_date = artist['B'].title().split('(')
        new_item['Name'] = list(reversed(name_date[0].split()))
        years = name_date[-1].strip('()').split('-')
        new_item['Life'] = years
        new_item['TotalSold'] = int(re.sub("[^0-9]", "", artist['C']))
        new_item['TotalLots'] = int(re.sub("[^0-9]", "", artist['E']))
        new_item['MaxPrice'] = int(re.sub("[^0-9]", "", artist['G']))
        new_item['SaleYear'] = year
        return_list.append(new_item)
    return return_list



clean2009top500 = clean_data_extended(z, 2009)


def clean_extended(data):
    for artist in data:
        if artist['Name'][-1].isdigit():
            artist['Name'].pop()


clean_extended(clean2009top500)

file3 = '2008500.csv'
w = get_data(file3)
clean2008top500 = clean_data_extended(w, 2008)

clean_extended(clean2008top500)
