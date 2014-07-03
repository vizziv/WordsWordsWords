from bottle import get
from bottle import post
from bottle import request
from bottle import Bottle
from bottle import run
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

def letterCount(partial):
    matchWords = matches(partial)
    tallys = {}
    for (index,letter) in enumerate(partial):
        if letter == '.':
            wordTally = {}
            counter = 0
            for word in matchWords:
                wordTally.setdefault(word[index], 0)
                wordTally[word[index]] += 1.0
                counter += 1
            for i in wordTally:
                wordTally[i] = wordTally[i]/counter
            tallys[index] = wordTally 
    return tallys

app = Bottle()

@app.route('/')
def gimme():
    partial = request.query.get('partial')
    return(letterCount(partial))

run(app, host='0.0.0.0', port=8000)

