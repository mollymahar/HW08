#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################

import re

def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(d, v):
    allKeys = []
    for k in d:
        if d[k] == v:
            allKeys.append(k)
    return allKeys


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

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
        # using a regex to eliminate specific end-of-line punctuation chars followed
        # by any whitespace characters, but not eliminate the hyphen mid-word
        # (just invoking .split() leaves items like "try:")
        pledge_list.remove('')                         # remove any blank items
    return pledge_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, 1)
    print reverse_lookup_new(pledge_histogram, 9)
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
