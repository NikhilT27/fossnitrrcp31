Nikhil Thakare
Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
fossnitrrcp31

Code:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump_count_index = 0
    jump = 0
    if len(c) == 2:
        jump = 1
        return jump
    for i in range(len(c)):
        if i == jump_count_index:
            if i < len(c)-4:
                if c[i+2] == 0:
                    jump += 1
                    jump_count_index += 2
                else:
                    jump += 1
                    jump_count_index += 1
            elif i< len(c)-2:
                jump += 1
                jump_count_index += 1
        else:
            pass
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
