#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #you only need to convert the PM
    hour = int(s[0:2])
    period = s[-2:]
    new_hour = ""
    
    if period == "PM" and hour < 12:
        new_hour = str(hour+12) +s[2:-2]
    elif period == "AM" and hour == 12:
        new_hour = "00" + s[2:-2]
    else:
        new_hour = s[0:-2]
    
    return new_hour             
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
