#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    count =0
    obs = set([(x,y) for x,y in obstacles])
    dirs = [[-1,-1],[1,-1],[1,1],[-1,1],[1,0],[0,-1],[-1,0],[0,1]]
    
    for d in dirs:
        x = r_q
        y = c_q
        while(1):
            x+=d[0]
            y+=d[1]
            if x==0 or y==0 or x==n+1 or y==n+1:
                break
            if((x,y) in obs):
                break
            count+=1
    return count

if __name__ == '__main__':
    fptr = open('outputf.in', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
