# coding: utf-8

"""
    juli
    -----

    距离产生美。
"""

import string
import re

class characters:
    HALF_SEPRATOR = ' \t\n'
    HALF_ALPHA_NUMERIC = string.ascii_letters + string.digits
    FULL_PUNCTUATION = u'，、。？！“”‘i’：；（）ー−—―〜｜＊『』「」【】［］｛｝〔〕〈〉《》　＿＜＞／・｀＠＋＾％＆％＄￥＃'

(HALF_SEPRATOR, HALF_ALPHA_NUMERIC, HALF_OTHER, FULL_PUNCTUATION, FULL_OTHER) = TYPES = range(5)

def get_type(s):
    if s in characters.HALF_SEPRATOR:
        return HALF_SEPRATOR
    elif s in characters.HALF_ALPHA_NUMERIC:
        return HALF_ALPHA_NUMERIC
    elif ord(s) < 255:
        return HALF_OTHER
    elif s in characters.FULL_PUNCTUATION:
        return FULL_PUNCTUATION
    else:
        return FULL_OTHER

SHOULD_IGNORE = (
    (HALF_ALPHA_NUMERIC, HALF_OTHER),
    (HALF_ALPHA_NUMERIC, FULL_PUNCTUATION),
    (HALF_OTHER, FULL_PUNCTUATION),
)


pat = re.compile(r'\b')

def render(src):
    """ Add space between half-width and full-width characters.
    """
    def func(m):
        l, r = src[m.start()-1], src[m.end()]
        _types = tuple(sorted(map(get_type, (l, r))))
        if HALF_SEPRATOR in _types or _types in SHOULD_IGNORE:
            return ''
        return ' '

    return pat.sub(func, src)


if __name__ == '__main__':
    s = u'我在github上关注了123个repo。'
    print '%s\n=>\n%s' %(s, render(s))
