https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    charlist = ""
    idx = 0
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                charlist += i.upper()
            else :
                charlist += i.lower()
        else:
            idx = 0
            charlist += ' '
            continue

    return charlist

s = "try hello world"


isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴해주고, 
isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴해줍니다.