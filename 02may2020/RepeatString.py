# Nikhil Thakare
# Link: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# fossnitrrcp31

# Code:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    letter_in_subsequence = []

    for i in range(len(s)):
        letter_in_subsequence.append(s.count("a",0,i+1))
    
    divisible = n//len(s)
    remember = n%len(s)
    if remember != 0:
        remaining = int(letter_in_subsequence[remember-1])
    else:
        remaining = 0
    total_count = divisible * int(letter_in_subsequence[len(s)-1]) + remaining
    return total_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
