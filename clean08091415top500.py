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
        name_date = artist['B'].title().split()
        new_item['Name'] = list(reversed(name_date[:-1]))
        years = name_date[-1].strip('()').split('-')
        new_item['Life'] = years
        new_item['TotalSold'] = int(re.sub("[^0-9]", "", artist['C']))
        new_item['TotalLots'] = int(re.sub("[^0-9]", "", artist['D']))
        new_item['MaxPrice'] = int(re.sub("[^0-9]", "", artist['E']))
        new_item['SaleYear'] = year
        return_list.append(new_item)
    return return_list


# In[44]:


cleantop5002015 = clean_data(x, 2015)


# In[45]:


cleantop5002015[2]


# In[46]:


file1 = '2014top500.csv'
y = get_data(file1)
cleantop5002014 = clean_data(y, 2014)


# In[69]:


cleantop5002014[0]


# In[74]:


file2 = '2009500.csv'
z = get_data(file2)


# In[75]:


z[0]
# A, B, C, E, G


# In[76]:


def clean_data_extended(read_file, year):
    return_list = []
    for artist in read_file:
        new_item = {}
        new_item['Rank'] = int(artist['A'])
        name_date = artist['B'].title().split()
        new_item['Name'] = list(reversed(name_date[:-1]))
        years = name_date[-1].strip('()').split('-')
        new_item['Life'] = years
        new_item['TotalSold'] = int(re.sub("[^0-9]", "", artist['C']))
        new_item['TotalLots'] = int(re.sub("[^0-9]", "", artist['E']))
        new_item['MaxPrice'] = int(re.sub("[^0-9]", "", artist['G']))
        new_item['SaleYear'] = year
        return_list.append(new_item)
    return return_list


# In[77]:


cleantop5002009 = clean_data_extended(z, 2009)


# In[78]:


cleantop5002009[-1]


# In[72]:


def clean_extended(data):
    for artist in data:
        if artist['Name'][-1].isdigit():
            artist['Name'].pop()


# In[81]:


clean_extended(cleantop5002009)
cleantop5002009[-1]


# In[82]:


file3 = '2008500.csv'
w = get_data(file3)
cleantop5002008 = clean_data_extended(w, 2008)


# In[83]:


cleantop5002008[-1]


# In[84]:


clean_extended(cleantop5002008)


# In[85]:


cleantop5002008[-5]


# In[ ]:
