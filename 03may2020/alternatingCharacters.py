# Nikhil Thakare
# Link: https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen
# fossnitrrcp31

# Code:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    strlist = list(s)
    temp = []
    temp.append(strlist[0])
    deletion = 0

    for i in range(1,len(strlist)):
        if temp[len(temp)-1] == strlist[i]:
            deletion += 1
        else:
            temp.append(strlist[i])
    
    return(deletion)
    
    # A = s.count("A")
    # B = s.count("B")
    # if A == 0 or B == 0:
    #     return(A+B-1)
    # elif A == B:
    #     return(0)
    # elif abs(A-B) == 1:
    #     return(0)
    # elif abs(A-B)>1:
    #     return(abs(A-B)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
