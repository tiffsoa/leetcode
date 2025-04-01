#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    chars = {}
    
    
    for char in s.replace(" ", "").strip().lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
         
    if len(chars) == 26:
        return "pangram"
    return "not pangram"              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
