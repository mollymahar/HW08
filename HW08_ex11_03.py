#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

# imports
import re

# body

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
	keys_ordered = sorted(h.keys())
	for k in keys_ordered:
		print k, h[k]


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
        # using a regex to eliminate specific end-of-line punctuation chars that are followed
        # by any whitespace characters, but not eliminate the hyphen mid-word
        # (just invoking .split() leaves items like "try:")
        pledge_list.remove('')                                       # remove any blank items
    return pledge_list



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
