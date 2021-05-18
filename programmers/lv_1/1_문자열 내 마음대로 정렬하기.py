https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    n_answer = [] 		#n번째 문자를 저장하는 배열
    
    for string in strings:	#strings에 들어있는 단어를 하나씩 가져오기
        n_answer.append(string[n])	#단어의 n번째 문자를 n_answer에 저장하기
    
    n_answer.sort()			#n_answer를 오름차순으로 정렬하기
    
    for i in n_answer:		#정렬되어 있는 n_answer에 해당하는 문자와 
        for string in strings:	#strings에 해당하는 단어의 n번째 수가 같을 경우
            if string[n] == i:
                answer.append(string)	#그 순서대로 answer배열에 저장
          
    return answer

def solution(strings, n):
    return sorted(strings, key=lambda x: x[n])


def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]    
    
    strings.sort()
    for j in range(len(strings)):
        answer.append(strings[j][1:])    
    
    return answer

['cabcd', 'cabce', 'xcdx']
['abcd', 'abce', 'cdx']