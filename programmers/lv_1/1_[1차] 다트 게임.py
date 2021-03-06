https://programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')    
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: # 맨처음은 건너 뜁니다~, dart=[1,...] 형태 drat[i-1] i는 1부터~
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

dartResult = '1D2S#10S'
print(solution(dartResult))

https://wikidocs.net/4308 정규식 표현