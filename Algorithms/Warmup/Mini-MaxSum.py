#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    
    minArr = min(arr)
    maxArr = max(arr)
    arr.remove(minArr)
    arr.remove(maxArr)
    
    sum = 0
    
    for i in arr:
        sum += i
    
    print(sum + minArr, sum + maxArr)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
