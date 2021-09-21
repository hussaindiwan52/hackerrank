#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(n,a):
    print(a)
    maxlen=0
    len=0
    for i in range(0,n):
        len=0
        for j in range(i,n):
            if abs(a[i]-a[j])<=1:
                len+=1
        if maxlen<=len:
            maxlen=len
    return maxlen
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    a.sort()
    result = pickingNumbers(n,a)

    fptr.write(str(result) + '\n')

    fptr.close()
