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
    soup = get_soup(f'https://www.artprice.com/artprice-reports/the-art-market-in-2016/top-500-artists-by-auction-revenue-2016/top-500-{start}-to-{end}/')
    return soup.find('tbody').find_all('tr')

# does dictionary thing
def populate_artist_price_info_sales(to_populate, artist_soup, table_head):
    for artist in artist_soup:
        artist_info = artist.find_all('td')
        artist_dict = {}
        for i in range(len(artist_info)):
            artist_dict[table_head[i]] = artist_info[i].text
        artist_dict['SaleYear'] = 2016
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

url2016 = 'https://www.artprice.com/artprice-reports/the-art-market-in-2016/top-500-artists-by-auction-revenue-2016/top-500-1-to-50/'
soup2016 = get_soup(url2016)
titles2016 = ['Rank', 'Name', 'TotalSold', 'TotalLots', 'MaxPrice']
to_clean2016 = ['Rank','TotalSold', 'TotalLots', 'MaxPrice']

final_2016 = run_through(titles2016)
clean_list(final_2016, to_clean2016)
for artist in final_2016:
    # artist['Name'] = artist['Name'].title().split()[:-1])
    artist['Name'] = artist['Name'].title().split('(')[0].split()

clean2016top500 = final_2016
