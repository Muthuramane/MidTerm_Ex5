__author__ = 'muthuraman.e'


#!/usr/bin/env python
# $Id: ddmin.py,v 2.2 2005/05/12 22:01:18 zeller Exp $

from split import split
from listsets import listminus
import re

PASS       = "PASS"
FAIL       = "FAIL"
UNRESOLVED = "UNRESOLVED"

def ddmin(circumstances, test):
    """Return a sublist of CIRCUMSTANCES that is a relevant configuration
       with respect to TEST."""

    #assert test([]) == PASS
    #assert test(circumstances) == FAIL

    #print "ddmin: Entry"
    #print "circumstances: ", circumstances
    #print "test: ", test

    n = 2
    while len(circumstances) >= 2:
        subsets = split(circumstances, n)
        assert len(subsets) == n

        #print "ddmin: subsets ", subsets

        some_complement_is_failing = 0
        for subset in subsets:
            complement = listminus(circumstances, subset)

            #print "ddmin: complement: ", complement

            #if test(complement) == FAIL:
            if test(complement) == PASS:
                circumstances = complement
                n = max(n - 1, 2)
                some_complement_is_failing = 1
                break

        if not some_complement_is_failing:
            if n == len(circumstances):
                break
            n = min(n * 2, len(circumstances))

    #print "Circumstances: ", circumstances
    #print "ddmin: Exit"
    return circumstances



if __name__ == "__main__":
    tests = {}
    circumstances = []

    def string_to_list(s):
        #print "string_to_list: Entry"
        c = []
        for i in range(len(s)):
            c.append((i, s[i]))
        #print "string_to_list: C: ", c
        #print "string_to_list: Exit"
        return c

    def findACharCount(str, fChar):
        count = 0
        #print "findACharCount: Entry"

        for chr in str:
            if chr == fChar:
                count += 1

        #print "Count: ", count
        #print "findACharCount: Exit"
        return count

    def mytest(c):
        global tests
        global circumstances

        #print "mytest: Entry"

        s = ""
        for (index, char) in c:
            s += char

        #print "mytest: S: ", s

        if s in tests.keys():
            #print "mytest: s: ", s
            #print "mytest: Exit"
            return tests[s]

        map = {}
        for (index, char) in c:
            map[index] = char

        #print "mytest: map: ", map

        x = ""
        for i in range(len(circumstances)):
            if map.has_key(i):
                x += map[i]
            else:
                x += "."

        print "%02i" % (len(tests.keys()) + 1), "Testing", `x`,

        if s != "" :
            gCount = findACharCount(s, 'g')
            eCount = findACharCount(s, 'e')

            if gCount >= 3 or eCount >=2:
                print PASS
                tests[s] = PASS
                #print "mytest: Exit"
                return PASS

        print FAIL
        tests[s] = FAIL
        #print "mytest: Exit"
        return FAIL


    print "<<<<<<< Delta Debugging >>>>>>>"
    deltaString = raw_input("Input delta debug string: ")

    if len(deltaString) < 16:
        print "Delta Debugging required more than 16characters"
        exit(0)

    deltaString = deltaString[:16]
    circumstances = string_to_list(deltaString)
    #print circumstances
    mytest(circumstances)
    print ddmin(circumstances, mytest)
