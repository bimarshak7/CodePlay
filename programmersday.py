#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def julian(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True
def g(year):
    if year%400 or (year%4==0 and year%100!=0):return True
    return False
def dayOfProgrammer(year):
    # Write your code here
    if year<1917:
        l = julian(year)
    else:
        l = g(year)
    if l==True:
        day = 12
    else:
        day = 13
    return str(day)+".09."+str(year)
        

if __name__ == '__main__':
    fptr = open('outputf.in', 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
