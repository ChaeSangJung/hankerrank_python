https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'

2로 나눴을 때 나머지가 1이면 True를 반환하기 때문에 (Bool 자료형), 1을 반환할 경우 홀수 아니면 짝수

def solution(num):
    if num % 2:
        return 'Odd'
    else:
        return 'Even'