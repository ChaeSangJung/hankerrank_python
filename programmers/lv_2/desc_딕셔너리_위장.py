https://programmers.co.kr/learn/courses/30/lessons/42578

문제 지문 파악하기
이 문제에서 중요한 것은 2가지입니다.

입력은 "옷, 파츠" 쌍의 2차원 배열입니다.
옷의 이름은 1개입니다.
이 문제는 "해시 + 경우의 수"로 풀 수 있습니다. 무슨 말이냐, 첫 번째 입력을 보겠습니다.

입력 : [ ["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"] ]

이 들어온 입력에 대해서 { 파츠 : 옷의 개수 } 쌍으로 저장하는 해시를 만들어 줍니다.

입력을 통해 만들어지는 해시 : { "headgear" : 2, "eyewear" : 1 }

이 때, 각 파츠를 조합해서 만들 수 있는 경우의 수를 도입하면 됩니다. 경우의 수는 다음과 같은 수식이 성립합니다.

경우의 수  = ( 파츠 1의 옷의 개수 + 1 ) x ( 파츠 2의 옷의 개수 + 1 ) x .. x (파츠 N의 옷의 개수 + 1) - 1

즉 이 입력에 대한 결과는 3( "headgear" 파츠의 옷의 개수 2개 + 1) x 2 ("eyewear" 파츠의 옷의 개수 1개 + 1) - 1 = 5개가 됩니다.

def solution(clothes):	
    d = dict()
    
    for _, body in clothes:        
        d[body] = d.get(body, 0) + 1
    
    
    answer = 1
    for v in d.values():
        answer *= (v + 1)
    
    return answer-1

https://wikidocs.net/16
02-5 딕셔너리 자료형