#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    bins = 1
    w.sort()
    curr_min = w[0]
    for i in range(len(w)):
        if w[i] > curr_min + 4:
            bins += 1
            curr_min = w[i]
            
    return bins

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
