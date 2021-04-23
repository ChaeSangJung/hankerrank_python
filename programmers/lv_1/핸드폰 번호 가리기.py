https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    num = len(phone_number)
    back = phone_number[-4:]
    
    return "*"*(num-4)+back

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]