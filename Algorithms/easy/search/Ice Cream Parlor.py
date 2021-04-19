https://www.hackerrank.com/challenges/icecream-parlor/problem

def icecreamParlor(m, arr):
    result = []
    
    index_prev = -1
    index_next = -1

    for i in range(len(arr)):
        for j in range(len(arr)):    
            if i != j and arr[i] + arr[j] == m:
                index_prev = i+1
                index_next = j+1
                result.append(index_prev)
                result.append(index_next)
                break
        if index_prev != -1 and index_next != -1:
            break
    
    return result