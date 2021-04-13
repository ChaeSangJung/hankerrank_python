https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_num =0
    orange_num = 0
    for i in range(len(apples)):
        apples[i] += a
    for i in range(len(oranges)):
        oranges[i] += b    
    
    
    for distance in apples:        
        if(s <= distance and distance <= t):            
            apple_num +=1
    
    for distance in oranges:
        if(s <= distance and distance <= t):
            orange_num +=1
    
    print(apple_num)
    print(orange_num)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
