#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

	remainder = n % len(s)

	perString = s.count("a")
	inRemainder = 0
	if remainder > 0:
		inRemainder = s[:remainder].count("a")

	return int(n / len(s)) * perString + inRemainder



if __name__ == '__main__':

    s = "aba"

    n = 10

    result = repeatedString(s, n)
    print(result)