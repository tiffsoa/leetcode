#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    chars = list('abcdefghijklmnopqrstuvwxyz')
    rotated = {}
    
    for i, char in enumerate(chars):
        rotated[char] = chars[(i + k)%len(chars)]
    
    temp_s = s
    answer = ""
    
    for i, letter in enumerate(temp_s.lower()):
        if letter not in rotated:
            answer += letter
        else:
            if s[i].isupper():
                answer += rotated[letter].upper()
            else:
                answer += rotated[letter]
    
    return answer                
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
    