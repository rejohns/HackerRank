#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    pCount = 0
    nCount = 0
    
    for i in arr:
        if i > 0:
            pCount += 1
        elif i < 0:
            nCount += 1
            
    print("{:1.6f}".format(pCount / len(arr)))
    print("{:1.6f}".format(nCount / len(arr)))
    print("{:1.6f}".format((len(arr) - pCount - nCount) / len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
