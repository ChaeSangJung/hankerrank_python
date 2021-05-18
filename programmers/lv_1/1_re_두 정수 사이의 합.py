https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    for item in range(min(a,b), max(a,b)+1):
        answer += item
    return answer


def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

# range() 시작과 끝~