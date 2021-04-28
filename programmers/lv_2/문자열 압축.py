https://programmers.co.kr/learn/courses/30/lessons/60057

유사문제 "짝지어 제거하기" https://programmers.co.kr/learn/courses/30/lessons/12973

# 파이썬
def solution(s):
    LENGTH = len(s)
    STR, COUNT = 0, 1
    cand = [LENGTH]  # 1~len까지 압축했을때 길이 값

    for size in range(1, LENGTH//2 + 1):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        # splited = []
        # for i in range(0, LENGTH, size):
        #   splited.append(s[i:i+size])
        stack = [[splited[0], 1]]

        for unit in splited[1:]:
            if stack[-1][STR] != unit:  # 이전 문자와 다르다면
                stack.append([unit, 1])
            else:  # 이전 문자와 다르다면
                stack[-1][COUNT] += 1

        compressed += ('').join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
        # for w, cnt in stack:          
        #     if cnt > 1:
        #         compressed += str(cnt) + w
        #     else:
        #         compressed += w
        cand.append(len(compressed))

    return min(cand)  # 최솟값 리턴

s= 'aabbaccc'

LENGTH 8 = len(s)
STR, COUNT = 0, 1
cand = [LENGTH] cand= [8]

for size in range(1, LENGTH//2 + 1:5):
    size = 1
    splited = [s[i 0:i 0+size 1:1] for i in range(0, LENGTH 8, size 1)]
    splited = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']

    stack = [[splited[0], 1]]
    stack = [['a',1]]

    for unit in splited[1:]: 'a', 'b', 'b', 'a', 'c', 'c', 'c']
        unit = 'a'
        if stack[-1][STR 0] 'a' != unit a false
        else:
            stack[-1][COUNT 0] += 1 : stack = [['a','2']]
        unit = 'b'
        if stack[-1][STR 0] 'a' != unit b true
            stack.append([unit 'b', 1]) : stack = [['a',2],'['b', 1]']
        unit = 'b'
            stack[-1][COUNT 0] += 1 : stack = [['a',2],'['b', 2]']
        unit = 'a'
        if stack[-1][STR 0] 'a' != unit a false
        else:
            stack[-1][COUNT 0] += 1 : stack = [['a',2],['b', 2],'['a',1]']
        unit = 'c'
        if stack[-1][STR 0] 'c' != unit a false
        else:
            stack[-1][COUNT 0] += 1 : stack = [['a',2],['b', 2],['a',1],['c',1]]
        unit = 'c'
        if stack[-1][STR 0] 'c' != unit c true
            stack = [['a',2],['b', 2],['a',1],['c',2]]
        unit = 'c'
        if stack[-1][STR 0] 'c' != unit c true
            stack = [['a',2],['b', 2],['a',1],['c',3]]
    
    compressed = '2a2ba3c'
    cnd = ['2a2ba3c']
