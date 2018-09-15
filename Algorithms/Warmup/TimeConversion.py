#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    time = s.split(":")

    if time[2][2] == "A" and time[0]== "12":
        time[0] = "00"

    if time[2][2] == "P" and time[0] != "12":
        time[0] = str(int(time[0]) + 12)
    
    if len(time[0]) == 1:
        time[0] = "0" + time[0]
    
    time[2] = time[2][0] + time[2][1]
    
    return time[0] + ":" + time[1] + ":" + time[2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
