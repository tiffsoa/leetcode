#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = 0
    max_sum = 0
    j = len(arr) - 1
    for i in range(len(arr)-1):
        min_sum += arr[i]
        
    while (j > 0):
        max_sum += arr[j]
        j -= 1
    
    print(f"{min_sum} {max_sum}")        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
