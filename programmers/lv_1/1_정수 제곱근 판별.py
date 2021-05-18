https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    num = pow(n, 0.5)

    if num == int(num) :
        return int((num+1)**2)

    return -1

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'