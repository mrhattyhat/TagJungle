import constants
import nltk
import operator
import re

from collections import Counter
from decorators import cached_property
from nltk import FreqDist
from nltk.tokenize import word_tokenize

class BaseAnalyzer(object):
    """
    NOTE: A list and descriptions of NLTK tags can be seen by invoking nltk.help.upenn_tagset()
    """
    def __init__(self, data):
        self.data = data

    @cached_property
    def tags(self):
        tags = nltk.pos_tag(self.text)
        return [t for t in tags if re.search('\w+', t[0])]

    @cached_property
    def terms(self):
        c = Counter([t[0] for t in self.tags if
                        t[1].startswith(constants.NOUN) or
                        t[1].startswith(constants.ADJECTIVE) or
                        t[1].startswith(constants.VERB) or
                        t[1].startswith(constants.PRONOUN)
                        ])
        return sorted(c.items(), key=operator.itemgetter(1), reverse=True)

    @cached_property
    def terms_normalized(self):
        total = sum([t[1] for t in self.terms])
        terms = dict((word, float(count)/total * 100) for word, count in self.terms)
        return sorted(terms.items(), key=operator.itemgetter(1), reverse=True)

    @cached_property
    def text(self):
        return nltk.Text(self.tokens)

    @cached_property
    def tokens(self):
        return word_tokenize(self.data)

    @cached_property
    def fd(self):
        return FreqDist(self.tokens)

    @cached_property
    def pos(self):
        parts_of_speech = dict()
        parts_of_speech['adjectives'] = self._counter(constants.ADJECTIVE)
        parts_of_speech['adverbs'] = self._counter(constants.ADVERB)
        parts_of_speech['nouns'] = self._counter(constants.NOUN)
        parts_of_speech['pronouns'] = self._counter(constants.PRONOUN)
        parts_of_speech['verbs'] = self._counter(constants.VERB)
        return parts_of_speech

    @cached_property
    def pos_normalized(self):
        parts_of_speech = dict()
        for k, v in self.pos.iteritems():
            total = sum([t[1] for t in self.pos[k]])
            terms = dict((word, float(count)/total * 100) for word, count in self.pos[k])
            parts_of_speech[k] = sorted(terms.items(), key=operator.itemgetter(1), reverse=True)
        return parts_of_speech

    @cached_property
    def extracted_info(self):
        sentences = []
        sent = nltk.sent_tokenize(self.data)
        sent = [word_tokenize(sent) for sent in sent]
        sent = [nltk.pos_tag(sent) for sent in sent]

        for s in sent:
            sentences.append([p for p in s if re.search('\w+', p[0])])

        return sentences

    def _counter(self, pos_tag):
        c = Counter(i[0] for i in self.tags if i[1].startswith(pos_tag))
        return sorted(c.items(), key=operator.itemgetter(1), reverse=True)