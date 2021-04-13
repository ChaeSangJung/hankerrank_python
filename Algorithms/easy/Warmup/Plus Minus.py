https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in range(n):
        if arr[i] == 0:
            zero +=1
        elif arr[i] < 0:
            negative +=1
        else:
            positive +=1
    
    print(round((positive/n), 6))
    print(round((negative/n), 6))
    print(round((zero/n), 6))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
