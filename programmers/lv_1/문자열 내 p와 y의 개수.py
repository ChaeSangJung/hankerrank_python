https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

from collections import Counter
def numPY(s):
    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p']

def numPY(s):
    # 함수를 완성하세요
    s = s.lower()
    num_p = s.count('p')
    num_y = s.count('y')
    if num_p == num_y: return True
    else: return False