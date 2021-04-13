https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hour, minute, sec_amppm = s.split(':')
    ds = sec_amppm[0:2]
    dt = sec_amppm[2:]

    if(dt == "PM" and hour == "12" ):
        hour = "12"
    elif(dt == "PM" and hour != "12" ):
        hour = str(int(hour)+12)
    elif(dt == "AM" and hour =="12"):
        hour ="00"
    
    date = hour + ":" + minute + ":" + ds

    return date

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
