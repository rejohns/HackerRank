#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    
    for i in range(len(grades)):
        grade = int(grades[i])
        if grade % 5 > 2 and grade >= 38:
            grades[i] = grade + 5 - (grade % 5)
        else:
            grades[i] = grade
            
    return grades
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
