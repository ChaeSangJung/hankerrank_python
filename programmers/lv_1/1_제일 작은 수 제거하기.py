https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) > 1 :
        arr.pop(arr.index(min(arr)))
        return arr
    else :
        return [-1]

# index 확실히 알아 놓을 것