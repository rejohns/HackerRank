#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    
    for i in range (int(len(s) / 2)): # problems: mid, small inputs?
        if s[i] != s[-1 * (i+1)]:
            print (i, s[i+1:len(s)-i])
            if isPalindrome(s[i+1:len(s)-i]):
                return i
            else:
                return len(s) - (i + 1)
    return -1

def isPalindrome(s):
    for i in range (int(len(s) / 2)): # problems: mid, small inputs?
        if s[i] != s[-1 * (i+1)]:
            return False
    return True


if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
