https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = sum(arr)
    n = len(arr)
    answer = answer/n
    return answer

def average(list):
    if len(list) == 0:
        return 0

    return sum(list) / len(list)