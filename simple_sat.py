# -*- coding: utf-8 -*-
"""
Created on Sun May 27 2018
@author: Andras Horvath

"""


from __future__ import division



def GetData(STR):
    # get letters
    Letters = [ x for x in STR if x in "abcde" ]
    seen = set()
    seen_add = seen.add
    Letters = [ x for x in Letters if not (x in seen or seen_add(x)) ]
    # replace letters
    for i in range(len(Letters)):
        STR = STR.replace(Letters[i], "{{{0:d}}}".format(i))
    # replace operators
    d = {"|" : " or ", "&" : " and ", "~" : " not "}
    for i in d:
        STR = STR.replace(i, d[i])
    return { "Letters" : Letters, 
             "Operators" : STR,
             "Size" : len(Letters)}


    
def Permute(l):
    # permute a list
    if len(l) == 0:
        return [[]]
    permuted = [ l[0:1] + x for x in Permute(l[1:]) ]
    for i in range(1, len(l)):
        if l[i] == l[0]:
            continue
        l[0], l[i] = l[i], l[0]
        permuted += [ l[0:1] + x for x in Permute(l[1:]) ]
    return permuted
   
   
   
def GenTestMatrix(Size):
    # Create boolean test matrix
    Permutations = []
    for i in range(int(Size / 2) + 1):
        ones = [ True for j in range(i) ]
        zeros = [ False for j in range(Size - i) ]
        P = Permute(ones + zeros)
        if i < Size / 2:
            # create inverted boolean lists
            invP = map(lambda x: map(lambda y: not y, x), P)
        Permutations += P + invP
    return Permutations
    
    

def SimpleSAT(STR):
    Data = GetData(STR)
    M = GenTestMatrix(Data["Size"])
    # test all possible variable combinations
    for row in M:
        if eval(Data["Operators"].format(*row)):
            return "yes"
    return "no"



test0 = "(a&b)|c"
test1 = "(a&b&c)|~a"
test2 = "a&(b|c)&~b&~c"
test3 = "(a&c)&~a"
test4 = "(a&c&b)&(~a&d)"

print SimpleSAT(test0)
print SimpleSAT(test1)
print SimpleSAT(test2)
print SimpleSAT(test3)
print SimpleSAT(test4)