#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary_num = f'{n:032b}' #returns a string
    #n is the decimal number, 0 is what to put and 32 is the
    #length of the binary number, b converts to binary
    print(binary_num)
    temp = list(binary_num)
    
    for i, char in enumerate(temp):
        if char == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
    
    num = ''.join(temp)
    
    return int(num, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
