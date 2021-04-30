https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:        
        dic[hash(part)] = part        
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

participant	= ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))