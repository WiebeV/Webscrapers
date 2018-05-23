from bs4 import BeautifulSoup
import urllib3
from tqdm import tqdm
import datetime
import sys

current_year = int(datetime.datetime.now().year)
first_year = 1898
for year in tqdm(range(first_year, current_year + 1)):
    sys.stdout = open('./Data/IMDB/IMDB_Top_50_' + str(year) + '.txt', 'w')

    url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
    ourUrl = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(ourUrl, "lxml")

    movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

    i = 1
    print('Top 50 movies IMDB of {}'.format(year))
    for div_item in tqdm(movieList):
        div = div_item.find('div', attrs={'class': 'lister-item-content'})
        title = div.findChildren('h3', attrs={'class': 'lister-item-header'})
        try:
            score = div.find('div', attrs={'class': 'ratings-bar'}).findChildren('strong')
        except:
            pass
        print('Movie {}: {}'.format(i, title[0].findChildren('a')[0].contents[0]))
        try:
            print('Score: {}'.format(score[0].contents[0]))
            del score
        except:
            pass
        i += 1