https://www.hackerrank.com/challenges/between-two-sets/problem
https://junho85.pe.kr/1534

#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd 

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def chk_a(number, a):
  for i in a:
    if number%i != 0:
      return False
    else:
        return True

def chk_b(number, b):
  for j in b:
    if j%number != 0:
      return False
    else:
        return True

def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)

    tmp = max_a
    probe = max_a
    res = 0
    # Write your code here
    while tmp <= min_b:    
        if chk_a(tmp, a) and chk_b(tmp, b):
            res += 1  

        tmp += max_a
    
    return res

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

