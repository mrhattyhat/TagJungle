import constants

from acquire.wikiwrapper import WikiWrapper

class TestEntityAnalyzer:

    def test_gender(self):
        mitt = WikiWrapper.search('Mitt Romney', 1)
        assert mitt.gender == constants.GENDER[0]
