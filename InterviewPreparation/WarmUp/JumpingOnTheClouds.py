#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

	currCloud = 0
    jumps = 0

    while currCloud < len(c) - 1:
        if currCloud + 2 < len(c):
            if c[currCloud + 2] != 1:
                jumps += 1
                currCloud += 2
            else:
                jumps += 1
                currCloud += 1
        else:
            jumps += 1
            currCloud = len(c)

    return jumps


if __name__ == '__main__':

    n = 7

    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    print("*", result)
