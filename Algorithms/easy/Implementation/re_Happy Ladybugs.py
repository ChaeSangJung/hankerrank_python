https://www.hackerrank.com/challenges/happy-ladybugs
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    counter = Counter(b)
    for key, value in counter.items():
        if key != "_" and value == 1:
            return "NO"
     
    if "_" in b:
        return "YES"
 
    for idx in range(1, len(b)):
        if b[idx] == b[idx-1] or b[idx] == b[idx+1]:
            continue
        else:
            return "NO"
         
    return "YES"
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
