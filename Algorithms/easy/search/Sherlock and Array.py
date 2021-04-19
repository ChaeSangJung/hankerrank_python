https://www.hackerrank.com/challenges/sherlock-and-array/problem

def balancedSums(arr):
    res = 'NO'
    right = sum(arr)
    left = 0
    
    for el in arr:
        right -= el
        
        print("left = {} el = {} right = {}".format(left, el, right))
        if right == left:
            res = 'YES'
            break
            
        left += el
            
    return res