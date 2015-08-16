#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

import re

def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = {}
    for key, val in sorted(d.items()):              # use sorted so the words will appear in alpha order
        inverse.setdefault(val, []).append(key)
        # default is set to [], so if that value does not appear in inverse yet, 
        # it will create a [] and then append. If that value does already appear,
        # it will append to the existing list.
    return inverse


def print_hist_newest(d):
    sorted_values = sorted(d.keys())
    for k in range(sorted_values[0], sorted_values[-1] + 1):    # 1st to final value, inclusive
        print str(k) + ":", d.setdefault(k,'')  
        # setdefault will handle the exception of no value by printing empty string


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
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
