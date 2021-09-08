#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    lst=[0,0,0]
    for i in range(len(arr)):
        if arr[i]>0:
            lst[0]+=1/len(arr)
        if arr[i]<0:
            lst[1]+=1/len(arr)
        if arr[i]==0:
            lst[2]+=1/len(arr)
    print(lst[0])
    print(lst[1])
    print(lst[2])
           
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
