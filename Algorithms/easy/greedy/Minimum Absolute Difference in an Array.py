https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

def minimumAbsoluteDifference(arr):
    arr.sort()
    #initiate value using the first two element
    min_dif = abs(arr[0] - arr[1])
    #go over the sorted list and compare the distance between neighbors
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min_dif:
            min_dif = dif
    return min_dif

arr= [1, -3, 71, 68, 17]