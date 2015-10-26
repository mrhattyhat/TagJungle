import os
import requests

from bs4 import BeautifulSoup


class Reader(object):

    def __init__(self, uri, soup=True):
        base_path = os.path.join(os.path.dirname(__file__), 'data')
        try:
            f = open(os.path.join(base_path, uri), 'r')
            data = f.read()
            f.close()
        except IOError, e:
            if not uri.startswith('http'):
                url = 'https://' + os.path.basename(uri).strip('.data')
            else:
                url = uri
                uri = os.path.join(base_path, 'tmp.txt')
            req = requests.get(url, headers={'User-Agent': "Magic Browser"})
            data = req.text

            with open(uri, 'w') as data_file:
                data_file.write(data)

        self.data = data
        if soup:
            self.soup = BeautifulSoup(self.data)