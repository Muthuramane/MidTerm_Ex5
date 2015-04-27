#!/usr/bin/env python
# $Id: split.py,v 2.2 2004/07/17 11:09:18 zeller Exp $

def split(circumstances, n):
    """Split a configuration CIRCUMSTANCES into N subsets;
       return the list of subsets"""
    #print "split: Entry"
    #print "Circumstances: ", circumstances
    #print "n: ", n

    subsets = []
    start = 0
    for i in range(0, n):
        len_subset = int((len(circumstances) - start) / float(n - i) + 0.5)
        subset = circumstances[start:start + len_subset]
        print subset
        subsets.append(subset)
        start = start + len(subset)

    assert len(subsets) == n
    for s in subsets:
        assert len(s) > 0

    #print "Subsets: ", subsets
    #print "split: Exit"

    return subsets
