#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    
    max_topics = 0
    max_topics_combs = 0
    
    for ind1 in range(len(topic)):
        for ind2 in range(ind1+1, len(topic)):
            person1 = topic[ind1]
            person2 = topic[ind2]
            temp_count = 0
            for k in range(len(person1)): # Hammond distance or something? Could be faster
                if person1[k] == "1" or person2[k] == "1":
                    temp_count += 1
            if temp_count > max_topics:
                max_topics = temp_count
                max_topics_combs = 1
            elif temp_count == max_topics:
                max_topics_combs += 1
                    
    return max_topics, max_topics_combs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
