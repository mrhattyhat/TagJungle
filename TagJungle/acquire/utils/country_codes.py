import csv
import json
import os

from acquire.reader import Reader
from decorators import cached_property
from pathlib import Path


class CountryCodes(object):
    BASE_PATH = os.path.join(str(Path(__file__).parents[1]), 'data')
    URI = os.path.join(BASE_PATH, 'countrycode.org.data')
    CODE_FILE = os.path.join(BASE_PATH, 'country_codes.txt')

    @staticmethod
    def update_country_codes():
        reader = Reader(CountryCodes.URI)
        rows = reader.soup.findAll('tr')

        with open(CountryCodes.CODE_FILE, 'w') as code_file:
            writer = csv.writer(code_file)
            for r in rows:
                c = r.findAll('td')
                if c:
                    abbrevs = c[2].text.split('/')
                    code = [c[0].text, c[1].text, abbrevs[0].strip(), abbrevs[1].strip()]
                    writer.writerow(code)

    @staticmethod
    def write_json():
        codes = list()
        with open(CountryCodes.CODE_FILE, 'r') as code_file:
            reader = csv.reader(code_file)
            for row in reader:
                c = dict()
                c['country'] = row[0]
                c['code'] = row[1]
                c['abbrev'] = row[2]
                codes.append(c)
        data = json.dumps(codes)

        with open(CountryCodes.CODE_FILE, 'w') as code_file:
            code_file.write(data)

        print 'Done'

    @cached_property
    def codes(self):
        with open(CountryCodes.CODE_FILE, 'r') as code_file:
            data = json.loads(code_file.read())

        return data

    def get_countries(self, code):
        return [c['country'] for c in self.codes if c['code'] == str(code)]

    def get_codes(self, country):
        return [c['code'] for c in self.codes if c['abbrev'] == country.upper()]

if __name__ == '__main__':
    CountryCodes.update_country_codes()