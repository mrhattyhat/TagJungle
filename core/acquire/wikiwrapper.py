import os

import django
import wikipedia

django.setup()

from core.analyze.entity import EntityAnalyzer
from bs4 import BeautifulSoup
from core.models import *
from datetime import datetime

class WikiWrapper(object):
    DATADIR = os.path.join(os.path.dirname(__file__), 'data')

    @classmethod
    def search(cls, phrase, entity_type):
        phrase = phrase.strip()
        terms = phrase.split(' ')
        target = '_'.join([t.lower() for t in terms])
        try:
            f = open('{0}/{1}/{2}.txt'.format(cls.DATADIR, constants.ENTITY_TYPE[entity_type][1], target))
            page = f.read()
            f.close()
            content = page.decode('utf8', 'replace')
            f = open('{0}/{1}/{2}.html'.format(cls.DATADIR, constants.ENTITY_TYPE[entity_type][1], target))
            html = f.read()
            f.close()
            html = html.decode('utf8', 'replace')
        except IOError:
            page = None
            html = None
            for res in wikipedia.search(phrase):
                if res.lower() == phrase.lower():
                    page = wikipedia.page(phrase)
                    html = page.html()
                    break
            if page:
                f = open('{0}/{1}/{2}.txt'.format(cls.DATADIR, constants.ENTITY_TYPE[entity_type][1], target), 'w')
                f.write(page.content.encode('utf8', 'replace'))
                f.close()
                f = open('{0}/{1}/{2}.html'.format(cls.DATADIR, constants.ENTITY_TYPE[entity_type][1], target), 'w')
                f.write(html.encode('utf8', 'replace'))
                f.close()
                content = page.content
            else:
                raise Exception('No match found for {0}'.format(phrase))
        bs = BeautifulSoup(html)
        try:
            bday_str = bs.findAll('span', {'class': 'bday'})[0].text
            if len(bday_str) < 10:
                bday_str = '{0}-01'.format(bday_str)
            bday = datetime.strptime(bday_str, '%Y-%m-%d')
        except IndexError:
            pass
        try:
            dday_str = bs.findAll('span', {'class': 'dday'})[0].text
            dday = datetime.strptime(dday_str, '%Y-%m-%d')
        except IndexError:
            pass

        return EntityAnalyzer(content)