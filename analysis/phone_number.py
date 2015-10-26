import re


class PhoneNumber(object):

    number_ptn = '(\+?[0-9]{1})?([-. ]{1})?\(?[0-9]{3}\)?([-. ]{1})[0-9]{3}([-. ]{1})[0-9]{4}'

    @staticmethod
    def parse(number):
        ptn = re.compile('[^\d]')
        number = re.sub(ptn, '', number)
        cc = ''
        area = ''

        if len(number) == 7:
            ex_end = 3

        elif len(number) > 7:
            ex_end = 6

        if len(number) == 10:
            area = number[0:3]
        elif len(number) == 11:
            area = number[1:4]
            cc = number[0]

        exchange = number[-7:ex_end]
        suffix = number[-4:]

        return '{0} ({1}) {2}-{3}'.format(cc, area, exchange, suffix)

    @classmethod
    def extract_numbers(cls, txt):
        ptn = re.compile(cls.number_ptn)

        for m in re.finditer(ptn, txt):
            print '{0} - {1}'.format(m.start(), cls.parse(m.group(0)))
