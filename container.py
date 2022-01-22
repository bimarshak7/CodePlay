#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    l = len(container)
    col={}
    cont = []
    for i in range(l):
        col[i]=0
    for i in range(l):
        cont.append(sum(container[i]))
        for j in range(l):
            #print(container[i][j])
            col[j]+=container[i][j]
        #print(col)
    print("color: ",col)
    print("Container: ",cont)    
    r = list(col.values())
    r.sort()
    cont.sort()
    if r==cont:
        return "Possible"
    return "Impossible"

if __name__ == '__main__':
    fptr = open('outputf.in', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
