#!/bin/python3

### THE WEBSITE is HackerRank !!!!!!!!!!!!!!!!!!!!!!!!!!!!

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    
    for number in arr:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1
    
    print(round(positive/len(arr), 6))
    print(round(negative/len(arr), 6))
    print(round(zero/len(arr), 6))
                    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
