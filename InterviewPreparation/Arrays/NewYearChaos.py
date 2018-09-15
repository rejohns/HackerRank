#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

	currSwaps = 0

	for i in range(len(q)-1, -1, -1):

		if q[i] - (i+1) > 2:
			print("Too chaotic")
			return
		for j in range(max(0, q[i] - 2), i):
			if q[j] > q[i]:
				currSwaps += 1

	print(currSwaps)


if __name__ == '__main__':

	t = 5

	intList = [5,5]
	qList = [[2,1,5,3,4],[2,5,1,3,4]]

	for i in range(2):
		n = intList[i]

		q = qList[i]

		minimumBribes(q)