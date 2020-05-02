# Nikhil Thakare
# HackerRank WarmUp Challenge
# fossnitrrcp31
# LINK: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


# CODE:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    total_step = 0
    count_valley = 0
    count_mountain = 0
    valley = 0
    mountain = 0
    
    
    for step_type in s:
        if step_type == 'U':
            if total_step == sea_level:
                mountain = 1
            total_step += 1
        elif step_type == "D":
            if total_step == sea_level:
                valley = 1
            total_step -= 1
        
        if total_step == sea_level:
            count_valley += valley
            count_mountain += mountain
            valley = 0
            mountain = 0
    
    return count_valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
