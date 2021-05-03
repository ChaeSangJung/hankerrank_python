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

이 문제를 풀기 위한 적절한 자료구조인 해시를 적용하여 알고리즘 성능을 올려보겠습니다. 해시란 "키-값" 쌍으로 저장하는 형태의 자료구조입니다. 해싱 함수를 통해 키를 통해서 값을 가져오는데 O(1)의 시간이 걸리지요. 이제 어떻게 올릴것이냐.

 

이 문제에서 중요한 점은 앞서 언급했듯이 "동명 이인이 있을 수 있다"입니다. 이것과 해시를 이용하면 문제를 해결하는 쉽습니다. 등록한 참가자를 모두 해시에 저장합니다. 어떻게 저장하냐? { 이름 : 동명이인의 수 }로 저장합니다.

 

첫 번째 입력을 통해 살펴볼까요?

 

입력 :
      participant: ["leo", "kiki", "eden"]
      completion: ["eden", "kiki"]
 

이 경우 먼저 participant를 순회하여 이름을 키로 해시를 만듭니다.

 

participant를 순회하여 저장된 해시 값 :
    { "leo": 1, "kiki": 1, "eden": 1 }
 

그 후, completion을 순회하여 이름을 키로 쌍으로 저장된 "동명 이인의 수"의 수를 1 줄입니다.

 

completion을 순회하여 동명이인의 수를 줄인 해시 값 :
    { "leo": 1, "kiki": 0, "eden": 0 }
 

이렇게 해서, 동명이인의 수가 0이 아닌 값을 가진 키 "leo"를 반환하면 됩니다.

 

이어서 동명이인이 있는 세 번째 입력도 살펴보겠습니다.

 

입력 :
    participant: ["mislav", "stanko", "mislav", "ana"]
    completion: ["stanko", "ana", "mislav"]
 

먼저 participant를 순회하여 이름을 키로 해시를 만듭니다.

 

participant를 순회하여 저장된 해시 값 :
    { "mislav": 2, "stanko": 1, "ana": 1 }
 

그 후, completion을 순회하여 이름을 키로 쌍으로 저장된 "동명 이인의 수"의 수를 1 줄입니다.

 

completion을 순회하여 동명이인의 수를 줄인 해시 값 :
    { "mislav": 1, "stanko": 0, "ana": 0 }
 

이렇게 해서, 동명이인의 수가 0이 아닌 값을 가진 키 "mislav"를 반환하면 됩니다. 어떻게 알고리즘이 동작하는지 아시겠지요? 다음 절에서 실제로 문제를 풀어봅시다.

강사님의 알고리즘 풀이
'문제 지문 파악하기'에서 세운 알고리즘을 간단하게 나타내면 다음과 같습니다.

 

{ 이름: 같은 이름의 인원 수 } 쌍의 해시를 만듭니다.
등록한 사람 이름 목록 participant에 존재하는 사람 이름을 해시에 저장합니다.
완주한 사람 이름 목록 completion에 존재하는 사람 이름에 대해서 해시에 저장된 해당 이름의 인원 수를 1 줄입니다.
사전에 등록된 { 이름: 인원 수 } 쌍 중 인원 수가 0보다 큰 사람 이름을 반환합니다.
코드로 표현하면 다음과 같습니다.

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]