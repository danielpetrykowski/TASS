from bs4 import BeautifulSoup

import requests
BASE = 'https://scholar.google.com'


class Scholar(object):

    def __init__(self):
        self.csv_link = None


    def search(self, user):
        req = requests.get('%s/citations?hl=pl&user=%s' % (BASE, user))
        soup = BeautifulSoup(req.content, 'html.parser')
        try:
            article = soup.find_all('tr', {'class': 'gsc_a_tr'})
            print("Found results for user %s" % user)
        except Exception as e:
            print(e)
            
            
        for a in article:
            try:
                authorsDiv = a.find('td', {'class': 'gsc_a_t'}).find('div')
                authorsLine = authorsDiv.text.strip()
                authorTab = authorsLine.split(",")
                print(authorTab)
            except Exception as e:
                print(e)
            
            
#        self.csv_link = BASE + soup.find('a', {'id': 'tool-download'})['href']
#        article_list = soup.find('ol', {'id': 'results-list'})
#        results = []
#        [results.append(Article(a)) for a in article_list.find_all('li')]
#        return results
