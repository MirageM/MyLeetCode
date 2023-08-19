"""
A password string, pwd consists of binary characters(0s and 1s).
A cybersecurity expert is trying to determine the minimum number of chances required
to make the password secur. To do so, it mush be divided into substrings of non-overlapping,
even length substrings. Each substring can only
contain 1s or 0s, not a mix. This helps to ensure that the password is strong and less vulnerable
to hacking attacks.

Find the minimum number of characters that must be flipped in the password string. i.e changed from 0 o 1 or 1 to 0
to allow the string to be divided as described.

Note: A substring is a contiguous group of characters in a string.

Given pwd = "1110011000"
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinFlips' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING pwd as parameter.
#x

def getMinFlips(pwd):
    # Input: 1110011000 Output: 3
    # Input: 100110 Output: 3
    # Input: 101011 Output: 2
    flips_zero, flips_one = 0, 0
    for i in range(len(pwd)):
        expected_char = '0' if i % 2 == 0 else '1'
        if pwd[i] != expected_char:
            flips_zero += 1 if expected_char == '0' else 0
            flips_one += 1 if expected_char == '1' else 0
    return min(flips_zero, flips_one)
   




# def getMinFlips(pwd):
#     # Input: 1110011000 Output: 3
#     # Input: 100110 Output: 3
#     # Input: 101011 Output: 2
#     flips_zero, flips_one = 0, 0
#     for i in range(len(pwd)):
#         expected_char = '0' if i % 2 == 0 else '1'
#         if pwd[i] != expected_char:
#             flips_zero += 1 if expected_char == '0' else 0
#             flips_one += 1 if expected_char == '1' else 0
#     return min(flips_zero, flips_one)
#     '''
#     Fix this code where the input 100110 returns 3 instead of 2
#     '''


    
  
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pwd = input()

    result = getMinFlips(pwd)

    fptr.write(str(result) + '\n')

    fptr.close()
