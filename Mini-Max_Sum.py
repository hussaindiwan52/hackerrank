#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    dict={}
    lowest=0
    largest=0
    for i in range(len(arr)):
        sum=0
        for j in range (len(arr)):
            if j!=i:
                sum+=arr[j]
        dict[i]=sum
        if lowest> sum or lowest==0:
            lowest=sum
        if largest<sum or largest==0:
            largest=sum
        
    print(lowest,largest,)
            
            
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
