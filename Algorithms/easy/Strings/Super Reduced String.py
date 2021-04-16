https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i = 1
    
    if (len(s) == 1):
        return s

    while i < len(s):
        if ( s[i-1] == s[i] ):
            # if (len(s) == 2):
            #     return "Empty String"
            s = s[:i-1] + s[i+1:]    
            i = 1
        else:
            i += 1

    if len(s) == 0:
        return 'Empty String'
    else:
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()


s= "aaabccddd"

1. 
i=1

while 1<len(s):9
    if ( s[i:1-1]:a == s[i:1]:a):
        s = s[:i:1-1] + s[i:1+1:]
        s = '' + 'abccddd'
        i=1

while 1<len(s):7 i = 1
    if ( s[1-1]:a == s[1]:b):
        i=2

s= 'abccddd' i = 2
while 2<len(s):7
    if ( s[i:2-1]:b == s[i:2]:c):
        i=3

s= 'abccddd' i = 3
while 3<len(s):7
    if ( s[i:3-1]:c == s[i:3]:c):
        s = s[ :i:3-1] + s[i:3+1 :]
        s = ab + ddd
        i = 1

s = 'abddd' i = 1
while 1<len(s):5
    if ( s[i:1-1]:a == s[i:1]:b):
        i = 2

s = 'abddd' i = 2
while 2<len(s):5
    if ( s[i:2-1]:b == s[i:2]:d):
        i = 2

s = 'abddd' i = 3
while 3<len(s):5
    if ( s[i:3-1]:d == s[i:3]:d):
        s = s[ :i:3-1] + s[i:3+1 :]
        s = ab + d

s= 'abd' i = 3
while 3<len(s):3 false

return s