#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports
import re                                       # use a regex later to eliminate punctuation from words

# Body

def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def histogram_new(l):
    new_d = dict()
    for word in l:
        new_d[word] = 1 + new_d.get(word, 0)
    return new_d

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. Returns the list.
    """
    pledge_list = []
    with open('pledge.txt') as f:
        pledge_list = re.split("[\s.:,]\s*", f.read())                 
        # using a regex to eliminate specific end-of-line punctuation chars that are followed
        # by any whitespace characters, but not eliminate the hyphen mid-word
        # (just invoking .split() leaves items like "try:")
        pledge_list.remove('')                                       # remove any blank items
    return pledge_list

##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())

if __name__ == '__main__':
    main()
