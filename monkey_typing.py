#!/usr/bin/env python

def count_words(string, set):

    counter = 0
    b = list(set)
    for word in b:
        if word in string.lower():
            counter += 1
    return counter

assert count_words("How aresjfhdskfhskd you?", {'how', 'are', 'you', 'hello'}) == 3
assert count_words("Bananas, give me bananas!!!", {'banana', 'bananas'}) == 2
assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                   {'sum', 'hamlet', 'infinity', 'anything'}) == 1


