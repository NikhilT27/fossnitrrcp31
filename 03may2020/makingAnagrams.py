# Nikhil Thakare
# Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# fossnitrrcp31

# Code:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    large = []
    small = []
    if len(a) > len(b):
        large = list(a)
        small = list(b)
    else:
        small = list(a)
        large = list(b)
    
    temp_small = small[:]
    for s in small:
        if s in large:
            large.remove(s)
            temp_small.remove(s)
    
    total_delete = len(temp_small)+len(large)
    return(total_delete)
    
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
