https://www.hackerrank.com/challenges/append-and-delete/problem

#!/bin/python3

import math
import os
import random
import re
import sys

s=abcd
t=abcdert
k=10

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    start = 0
    ind = 0
    to_del = 0
    to_app = 0
    
    while ind < len(s) and ind < len(t) and s[ind] == t[ind]:
        ind += 1
    start = ind
    
    if start < len(s):
        to_del = len(s[start:])
        if to_del == len(s) and k - to_del >= len(t):
            return 'Yes'
    if start < len(t):
        to_app = len(t[start:])
    k -= to_del + to_app
    
    if k == 0 or (k > 0 and k % 2 == 0) or k >= 2*len(t):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()


s=["a","b","c","d"]
t=["a","b","c","d","e","r","t"]
k=9

start = 0
ind = 0
to_del = 0
to_app = 0

while ind < len(s) and ind < len(t) and s[ind] == t[ind]:
    ind += 1
start = ind


if start < len(s):
    to_del = len(s[start:])
    if to_del == len(s) and k - to_del >= len(t):
        print('Yes')
if start < len(t):
    to_app = len(t[start:])
k -= to_del + to_app

if k == 0 or (k > 0 and k % 2 == 0) or k >= 2*len(t):
    print('Yes')
else:
    print('No')


start = 4

if start 4 < len(s) 4:
if start 4 < len(t) 7:
    to_app = len(t[4:] 3) #['e', 'r', 't']
k 6 -= to_del 0 + to_app 3

# 3번을 더하고 3번을 빼주면 9번 채움 !!