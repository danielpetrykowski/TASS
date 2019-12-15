import csv
import urllib
from io import StringIO
from urllib.request import urlopen

from google_patent_scraper import scraper_class


def find_all_patents(inventors):
    """
    Find all patents with given inventors list.
    @param inventors: List of dictionary of inventors [{name, surname}]
    @return: dictionary with patents (key is patent id)
    """
    inv_url = ""
    for inventor in inventors[:-1]:
        inv_url += "(" + inventor['name'] + "%2B" + inventor['surname'] + ")%2BAND%2B"
    inv_url += "(" + inventors[-1]['name'] + "%2B" + inventors[-1]['surname'] + ")"

    url = "https://patents.google.com/xhr/query?url=q%3D{0}%26oq%3D{1}&exp=&download=true".format(inv_url, inv_url)

    ur = urllib.request.urlopen(url)

    data = ur.read()

    f = StringIO(data.decode())

    reader = csv.reader(f, delimiter=',')
    rows = list(reader)

    patents_dict = {}
    for patent in rows[2:]:
        p = {}
        for e, name in enumerate(rows[1][1:]):
            p[name] = patent[e]
        patents_dict[patent[0]] = p
    return patents_dict


def find_patent_by_id(patent_id):
    """
    @param patent_id: String with patent id
    @return patent dictionary
    """
    scraper = scraper_class()

    status, soup, url = scraper.request_single_patent(patent_id)
    patent_parsed = scraper.process_patent_html(soup)
    return patent_parsed


if __name__ == '__main__':
    # Example of use
    l1 = {'name': 'Iwona', 'surname': 'Skrzecz'}
    l2 = {'name': 'Boguslaw', 'surname': 'Szewczyk'}

    inv = list()
    inv.append(l1)
    inv.append(l2)

    print(find_all_patents(inv))
    print(find_patent_by_id('WO2004050692A3 '))
