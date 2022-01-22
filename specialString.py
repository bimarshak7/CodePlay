#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    c=n
    r=[1]*n
    seq=s[0]
    for i in range(1,n):
        if s[i]==s[i-1]:
            c+=len(seq)
            seq+=s[i]
        else:
            print(i)
            for j in range(len(seq)):
                print(i+j+1)
                if s[i+j+1]==seq[j]:c+=1
                else: 
                    seq=s[i]
                    break 
    return c
if __name__ == '__main__':
    fptr = open("outputf.in", 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
