#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

	pairs = 0
	socks = {}

	for sock in ar:
		if sock not in socks:
			socks[sock] = ar.count(sock)

	for sock in socks:
		pairs += int(socks[sock] / 2)


	return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
