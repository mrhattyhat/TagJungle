
ENTITY_TYPE = (
    (0, 'unknown'),
    (1, 'person'),
    (2, 'organization'),
    (3, 'location'),
    (4, 'publication'),
)

GENDER = (
    (0, 'male'),
    (1, 'female'),
)

LOCATION_TYPE = (
    (0, 'geographic'),
    (1, 'web'),
)

ORG_TYPE = (
    (0, 'commercial'),
    (1, 'non-Profit'),
    (2, 'religious'),
    (3, 'political'),
    (4, 'news'),
)

FEMALE_INDICATORS = 'she', 'her', 'hers', 'herself'

MALE_INDICATORS = 'he', 'him', 'his', 'himself'

NEUTRAL_INDICATORS = 'i', 'my', 'myself', 'our', 'us', 'we', 'me'

# PART OF SPEECH (POS) TAGS

# Adjectives
ADJECTIVE = 'JJ'
ADJECTIVE_COMPARATIVE = 'JJR'
ADJECTIVE_SUPERLATIVE = 'JJS'

# Nouns
NOUN = 'NN'
NOUN_PLURAL = 'NNS'
NOUN_PROPER_SINGULAR = 'NNP'
NOUN_PROPER_PLURAL = 'NNPS'

# Pronouns
PRONOUN = 'PRP'
PRONOUN_POSSESSIVE = 'PRP$'

# Adverb
ADVERB = 'RB'
ADVERB_COMPARATIVE = 'RBR'
ADVERB_SUPERLATIVE = 'RBS'

# Verbs
VERB = 'VB'
VERB_PAST = 'VBD'
VERB_PAST_PARTICIPLE = 'VBN'
VERB_PRESENT = 'VBG'
VERB_PRESENT_NOT_TPS = 'VBP'  # Not third-person singular (e.g. sue, twist, spill, cure, lengthen, spray)
VERB_PRESENT_TPS = 'VBZ'  # Third-person singular (e.g. marks, mixes, displeases, emerges, uses, speaks)