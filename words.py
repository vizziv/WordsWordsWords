import re
from collections import defaultdict

def _words_from_file(path):
    with open(path) as lines:
        return [l.strip() for l in lines]

def _buckets(xs, key):
    bs = defaultdict(list)
    for x in xs:
        bs[key(x)].append(x)
    return bs

_word_buckets = _buckets(_words_from_file('words.txt'), len)

def matches(partial):
    r = re.compile(partial)
    return filter(r.match, _word_buckets[len(partial)])
