자세히 읽으면 '두 글자'이면서 'alternating'(abab와 같이 서로 교차하면서 바뀌는 문자열)

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def validate(string):
    for ind in range(len(string)-1):
        if string[ind] == string[ind + 1]:
            return False
    return True

def alternate(string):
    str_set = set(list(string))
    variants = combinations(str_set, 2)
    max_res = 0
    
    for comb in variants:
        t = [c for c in string if c == comb[0] or c == comb[1]]
        #print("comb = {} t = {}".format(comb, t))
        if validate(t):
            max_res = max(max_res, len(t))
        
    return max_res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
