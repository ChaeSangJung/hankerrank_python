https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    a = []
    s = reversed(str(n))
    for i in s:
        a.append(int(i))
    return a

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]