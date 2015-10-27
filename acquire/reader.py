import dryscrape
import os

from bs4 import BeautifulSoup
from urlparse import urlparse


class Reader(object):

    def __init__(self, uri, soup=True):
        base_path = os.path.join(os.path.dirname(__file__), 'data')
        try:
            f = open(os.path.join(base_path, uri), 'r')
            data = f.read()
            f.close()
        except IOError, e:
            parts = urlparse(uri)
            base_url = '{0}://{1}'.format(parts.scheme, parts.netloc)
            sess = dryscrape.Session(base_url=base_url)
            sess.set_attribute('auto_load_images', True)
            page = parts.path if parts.path else '/'
            sess.visit(page)
            data = sess.driver.body()

            local_page = '{0}-{1}'.format(parts.netloc, os.path.basename(parts.path))
            local_file = os.path.join(base_path, local_page)

            with open(local_file, 'w') as data_file:
                data_file.write(data.encode('utf-8'))

        self.data = data
        if soup:
            self.soup = BeautifulSoup(self.data)