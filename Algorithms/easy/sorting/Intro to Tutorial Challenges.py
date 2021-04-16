https://www.hackerrank.com/challenges/tutorial-intro/problem

def introTutorial(V, arr):
    result = 0
    for i in range(0,len(arr)):
        if V == arr[i]:            
            result = i
            break
    return result