import constants

from core.analysis.base_analyzer import BaseAnalyzer
from decorators import cached_property

class EntityAnalyzer(BaseAnalyzer):

    @cached_property
    def gender(self):
        fc = sum(p[1] for p in self.pos['pronouns'] if p[0] in constants.FEMALE_INDICATORS)
        mc = sum(p[1] for p in self.pos['pronouns'] if p[0] in constants.MALE_INDICATORS)

        if fc > mc:
            return constants.GENDER[1]
        else:
            return constants.GENDER[0]

        return (None, None)
