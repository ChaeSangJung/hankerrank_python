https://www.hackerrank.com/challenges/find-the-median/problem?h_r=next-challenge&h_v=zen

def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr)//2]