# Generator function randomWord has as an argument list of words. It should return any random word from this list.
# Each time words are different until the end of the list is reached.
# Then words are taken from the initial list again.

import random

def randomWord(inputlist):
    if inputlist:
        while True:
            wordlist = list(inputlist)
            while wordlist:
                yield wordlist.pop(random.randint(0, len(wordlist)-1))
    else:
        yield None


list = ['book', 'apple', 'word']
next(random(list))
