#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

	currPos = 0
	valleyCount = 0

	for step in s:
		if step == "U":
			currPos += 1
			if currPos == 0:
				valleyCount += 1

		else:
			currPos -= 1

	return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
