import re
def eadibitan(word):
    c = r'[bcdfghjklmnpqrstvwxyz]'
    v = r'[aeiouy]' if word[-1] == 'y' else r'[aeiou]'
    lookahead_1c = r'(?={}{}|$)'.format(c, v)
    lookahead_2c = r'(?={}{}{}|{}{}|$)'.format(c, c, v, c, v)

    pat = [r'({})({}){}'.format(c, v, lookahead_1c),
           r'({})({})({}){}'.format(c, v, v, lookahead_1c),
           r'({})({})({})({}){}'.format(c, v, v, v, lookahead_1c),
           r'({})({})({}){}'.format(c, v, c, lookahead_2c),
           r'({})({})({})({}){}'.format(c, v, v, c, lookahead_2c),
           r'({})({})({})({})({}){}'.format(c, v, v, v, c, lookahead_2c),
           r'({})({})({}){}'.format(c, c, v, lookahead_1c),
           r'({})({})({})({}){}'.format(c, c, v, v, lookahead_1c),
           r'({})({})({})({})({}){}'.format(c, c, v, v, v, lookahead_1c),
           r'({})({})({})({}){}'.format(c, c, v, c, lookahead_2c),
           r'({})({})({})({})({}){}'.format(c, c, v, v, c, lookahead_2c),
           r'({})({})({})({})({})({}){}'.format(c, c, v, v, v, c,
                                                lookahead_2c),
           r'^({}+)'.format(v)]

    ins = [r'\2\1',
           r'\2\1\3',
           r'\2\1\3\4',
           r'\2\1\3',
           r'\2\1\3\4',
           r'\2\1\3\4\5',
           r'\2\3\1',
           r'\2\3\1\4',
           r'\2\3\1\4\5',
           r'\2\3\1\4',
           r'\2\3\1\4\5',
           r'\2\3\1\4\5\6',
           r'\1']

    new_word = ''
    for m in re.finditer('|'.join(pat), word):
        syllable = m.group()
        for idx, p in enumerate(pat):
            if bool(re.match(p, syllable)):
                new_syllable = re.sub(p, ins[idx], syllable)
                break
        new_word += new_syllable
    return new_word
