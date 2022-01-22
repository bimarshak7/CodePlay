#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s=s.replace(" ","")
    L = math.sqrt(len(s))
    r = math.floor(L)
    c = math.ceil(L)
    if r*c<len(s):
        r=c
    s=s+" "*(r*c-len(s))
    a=[]
    for i in range(r):
        a.append(s[i*c:i*c+c])
    #a[-1]=a[-1].replace(" ","")
    for x in a:
        print(x)
    e=""
    for i in range(c):
        for k in range(r):
            e+=a[k][i].replace(" ","")
        e+=" " 
    #print(r,c,len(s))
    print(e)
    return e

if __name__ == '__main__':
    fptr = open('outputf.in', 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
