#  Link: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Nikhil Thakare
#   fossnitrrcp31
# -------------------------------------
#
#  Code:
# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    newList = list(ar)
    unique = []
    count = 0
    for value in newList:
        if value not in unique:
            unique.append(value)
    for unique_value in unique:
        temp = newList.count(unique_value)
        count += temp//2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
