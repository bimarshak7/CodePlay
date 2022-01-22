#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    if(w.count(w[0])==len(w)):return "no answer"
    f=w[0]
    c=0
    for x in w:
        if x>f:
            c=1
            break
        f=x
    if c==0:return "no answer"
    word=list(w)
    for i in range(len(word)-1,0,-1):
        if word[i]>word[i-1]:
            a = [x for x in w[i:] if x>w[i-1]]
            swap = min(a)
            ind = word.index(swap,i)
            word[i-1],word[ind]=swap,word[i-1]
            if(w=='dkhc'):
                print(swap,word)
            break
        
    r = word[:i]+sorted(word[i:])
    print(r)
    #print(swap,22)
    #print(p)    
    #abdc->hcdk
    return ''.join(r)

if __name__ == '__main__':
    fptr = open("outputf.in", 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()