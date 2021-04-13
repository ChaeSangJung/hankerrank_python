https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):    
    sum = 0
    for i in range(len(bill)):
        if (i != k):
            sum +=bill[i]
    
    payment = sum/2

    if(payment != b):
        print(int(b-payment))
    elif (payment == b):
        print("Bon Appetit")
    
    
    
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
