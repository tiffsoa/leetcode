#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_left = 0
    sum_right = 0
    n = int(len(arr))
    k = 0
    for i in range(n):
        sum_left += arr[i][k]
        k+=1
    k=n-1
    print(n)
    for j in range(n):
        sum_right += arr[j][k]
        k-=1
    return abs(sum_left - sum_right)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
