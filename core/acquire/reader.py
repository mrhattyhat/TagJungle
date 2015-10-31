import dryscrape
import os

from bs4 import BeautifulSoup
from urlparse import urlparse


class Reader(object):

    def __init__(self, uri, soup=True):
        if not uri.startswith('http'):
            uri = 'http://{0}'.format(uri)
        data_path = os.path.join(os.path.dirname(__file__), 'data')
        url_parts = urlparse(uri)
        local_page = url_parts.netloc
        page = url_parts.path if url_parts.path else '/'
        base_url = '{0}://{1}'.format(url_parts.scheme, url_parts.netloc)

        if url_parts.path:
            local_page += '-' + os.path.basename(url_parts.path)

        if url_parts.query:
            local_page += '-' + url_parts.query.replace('=', '-')
            page = '{0}?{1}'.format(page, url_parts.query)

        try:
            f = open(os.path.join(data_path, local_page), 'r')
            data = f.read()
            f.close()
        except IOError, e:
            sess = dryscrape.Session(base_url=base_url)
            sess.set_attribute('auto_load_images', True)
            sess.visit(page)
            data = sess.driver.body()

            local_file = os.path.join(data_path, local_page)

            with open(local_file, 'w') as data_file:
                data_file.write(data.encode('utf-8'))

        self.data = data
        if soup:
            self.soup = BeautifulSoup(self.data)