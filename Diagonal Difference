#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rows=len(arr)
    columns=len(arr[0])
    ldiag,rdiag=0,0
    for i in range (0,rows):
        ldiag+=arr[i][i]
    i=0
    for k in range (columns,0,-1):
        rdiag+=arr[i][k-1]
        i+=1
    
    diff=ldiag-rdiag
    return(abs(diff))
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
