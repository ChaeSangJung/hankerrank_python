https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = ' ' 
    shap = '#'

    for i in range(n): 
        print(space * ((n-1)-i) + shap * (i+1))



if __name__ == '__main__':
    n = int(input())

    staircase(n)
