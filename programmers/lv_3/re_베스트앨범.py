https://programmers.co.kr/learn/courses/30/lessons/42579

https://gurumee92.tistory.com/159?category=782306

문제 지문 파악하기
이번 문제는 주어진 입력 음악의 genres, 음악의 플레이 횟수 plays를 이용하여 다음을 조건을 만족하는 리스트를 만드는 것입니다.

총 플레이 횟수가 많은 genre 별로 내림차순으로 정렬되어야 한다.
장르 내에서도 play 횟수 내림차순, 고유 번호 오름차순으로 정렬되어야 한다.
한 장르 당 최대 2개까지만 뽑아서, 플레이 목록을 만들 수 있다.
플레이 목록은 고유 번호로 하는 리스트이다.
이것들을 만족하는 리스트를 어떻게 만들 수 있을까요? 먼저 고유 번호는 각 배열의 인덱스를 뜻합니다. 입력에 대해서 표로 표현하면 다음과 같습니다.

인덱스	0	1	2 	3	4
장르	classic	pop	classic	classic	pop
플레이 횟수	500	600	150	800	2500

자 이제 먼저 총 플레이 횟수가 많은 장르별로 정렬해봅시다. 먼저 { 장르 : 총 재생 횟수 } 형태로 저장하는 해시를 만들어줍니다.

{ classic : 1450, pop : 3100 }

이 해시를 토대로 총 재생 횟수 역순으로 장르를 정렬합니다.

[ ("pop", 3100), ("classic", 1450) ]

이제 장르별로 플레이 목록들을 정렬하기 위해서 { 장르 : [ (재생횟수, 고유 번호) ] } 형태로 저장하는 해시를 만들어줍니다.

{ "classic" : [ { 500, 0 }, { 150, 2 }, { 800, 3 }, ], "pop" : [ { 600, 1 }, { 2500, 4 }, ] }

이제 여기서 각각 재생 횟수 내림차순, 고유 번호 오름차순 즉 1차 기준을 재생 횟수 만약 같을 시에는 고유 번호로 정렬합니다. 그럼 해시는 다음과 같아집니다.

{ "classic" : [ { 800, 3 }, { 500, 0 }, { 150, 2 }, ], "pop" : [ { 2500, 4 }, { 600, 1 }, ] }

여기서 아까 만들어두었던 "총 재생 횟수의 내림차순으로 정렬한 장르 정보를 순회하여, 최대 2개까지 고유번호를 뽑아서 리스트를 만듭니다.

[ 4, 1, 3, 0 ]

어떻게 동작하는지 아시겠나요? 여기서 중요한 것은 "어떻게 목록을 정렬할 것인가"입니다. 이는 각 언어가 제공하는 정렬 알고리즘을 통해 손쉽게 구할 수 있습니다.

def solution(genres, plays):
    answer = []
    # { 장르 : 총 재생 횟수 } 사전
    playsDict = {}
    # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
    d = { }

    # 사전들 초기화
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [ (play, i) ]
        
    # 재생 횟수 내림차순으로 장르별로 정렬
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in d[genre][:2] ]
    
    return answer


