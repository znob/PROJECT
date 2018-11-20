import requests
from bs4 import BeautifulSoup
import re

def get_soup(url):
        r = requests.get(url)
        c = r.content
        return BeautifulSoup(c, 'html.parser')

def get_table_head(soup):
    return [x.text for x in soup.find_all('th')]

#goes by 50...1-50, 51-100, takes year statement
def get_50_artists_soup(start, end):
    soup = get_soup(f'https://www.artprice.com/artprice-reports/the-art-market-in-2017/ranking-of-the-top-500-artists-by-auction-turnover-in-2017/top-500-artists-{start}-to-{end}/')
    return soup.find('tbody').find_all('tr')[1:-1]

# does dictionary thing
def populate_artist_price_info_sales(to_populate, artist_soup, table_head):
    for artist in artist_soup:
        artist_info = artist.find_all('td')
        artist_dict = {}
        for i in range(len(artist_info)):
            artist_dict[table_head[i]] = artist_info[i].text
        artist_dict['SaleYear'] = 2017
        to_populate.append(artist_dict)

def run_through(table_head):
    to_populate = []
    for i in list(range(1,500,50)):
        soup = get_50_artists_soup(i, i+49)
        populate_artist_price_info_sales(to_populate, soup, table_head)
    return to_populate

def clean_list(list_artist, items_to_clean):
    for artist in list_artist:
        for item in items_to_clean:
            artist[item] = int(re.sub("[^0-9]", "", artist[item]))

url2017 = 'https://www.artprice.com/artprice-reports/the-art-market-in-2017/ranking-of-the-top-500-artists-by-auction-turnover-in-2017/top-500-artists-1-to-50/'
soup2017 = get_soup(url2017)
titles2017 = ['Rank', 'Name', 'Country', 'TotalSold', 'TotalLots', 'MaxPrice', 'New Record']
to_clean2017 = ['Rank','TotalSold', 'TotalLots', 'MaxPrice']

final_2017 = run_through(titles2017)
clean_list(final_2017, to_clean2017)
for artist in final_2017:
    artist['Name'] = artist['Name'].title().split('(')[0].split()
    # if artist['Name'][-1] == '(B.':
    #     artist['Name'].pop()
clean2017top500 = final_2017
