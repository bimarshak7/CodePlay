#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#Ans: 1

def pageCount(n, p):
    # Write your code here
    c=0
    if p!=1 or p!=n:
        c+=min((n-p)//2,p//2)
        if n%2==0 and c==0:c+=1
    return c

if __name__ == '__main__':
    fptr = open('outputf.in', 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
