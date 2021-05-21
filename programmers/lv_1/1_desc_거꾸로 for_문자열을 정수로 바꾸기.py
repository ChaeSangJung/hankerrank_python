https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    return int(s)

def solution(s):
    result = 0

    for idx, number in enumerate(s[::-1]): # 거꾸로 for
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
        
        print(idx,number, result)
        # 0 4 4
        # 1 3 34
        # 2 2 234
        # 3 1 1234
        # 4 - -1234

    return result