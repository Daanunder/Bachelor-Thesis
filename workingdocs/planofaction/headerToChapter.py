#!/usr/bin/env python

from pandocfilters import toJSONFilter, RawInline

def latex(s):
    return RawInline('latex', s)

def changeHeader(key, value, format, meta):
    if key =='Header'and value[0] == 1 and f == 'latex':
        return [latex('\\chapter{')] + v + [latex('}')]


if __name__ == "__main__":
    toJSONFilter(changeHeader)
