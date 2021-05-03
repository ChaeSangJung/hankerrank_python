https://programmers.co.kr/learn/courses/30/lessons/42626

heapq --- 힙 큐 알고리즘
https://python.flowdas.com/library/heapq.html

heapq는 일반적인 리스트와 다르게, 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬해주는 녀석이다.

import heapq 
def solution(scoville, K): 
    answer = -1 
    count = 0 
    check_flag = False 
    heapq_scoville = heapq.heapify(scoville) 
    
    while scoville[0] < K: 
        min_first = heapq.heappop(scoville) 
        min_second = heapq.heappop(scoville) 
        heapq.heappush(scoville, min_first + (min_second * 2)) 
        
        if len(scoville) == 1 and scoville[0] < K: 
            check_flag = True 
            break 
        count = count + 1 
    if check_flag == False: 
        answer = count 
    
    return answer

문제 지문 파악하기
문제의 입력을 통해서, 문제를 어떻게 풀어야할지 생각해봅시다.
 

문제 입력 :
scoville = [1, 2, 3, 9, 10, 12]
K=7

scoville에서 K보다 작은 수는 1, 2, 3이 존재합니다. 
따라서 scoville을 섞어주어야 합니다. 
scoville에서 가장 작은 원소 1과, 두번째로 작은 원소 2를 꺼냅니다. 
그 후 다음 수식을 적용시켜서 값을 저장합니다.

수식 : 가장 작은 원소 + (두 번째로 작은 원소 * 2)

즉, 수식을 적용하면 "1 + 2*2 = 5"가 되어 5라는 값을 다시 힙에 저장시키는 것이죠. 힙의 상태는 다음과 같습니다.

현재 상태 :
scoville = [3, 5, 9, 10, 12]
섞은 횟수 = 1번

아직 7보다 작은 수가 scoville에 존재합니다. 따라서 1번 더 섞도록 하죠. 이때, first = 3, second = 5이기 때문에 13(3 + 5 * 2)을 저장하게 됩니다.

현재 상태 :
scoville = [9, 10, 12, 13]
섞은 횟수 = 2번

이제 scoville에서 K인 7보다 작은 수는 없습니다. 
따라서 답 answer는 총 섞은 횟수 2를 반환하면 됩니다.
 여기서 중요한 점은 데이터를 저장하고 삭제하는 과정에서 정렬 상태를 유지해야한다는 것입니다. 
 그럼 섞을 때마다, 정렬을 해주면 되겠군요! 즉, 다음처럼 풀수 있겠지요.

 def solution(scoville, K):
    answer = 0
    # 1. scoville 정렬
    scoville.sort()

    # 2. 스코빌 지수 섞기
    while scoville:
        first = scoville.pop(0)

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1
        
        second = scoville.pop(0)
        scoville.append(first + second * 2)
        scoville.sort()
        answer += 1
    
    return answer


이렇게 하면, 정확성 테스트는 모두 통과하지만, 효율성 테스트에서 모두 "시간 초과"라는 결과를 얻을 수 있습니다. 
이럴 때, 시간 복잡도는 O(N * Nlog(N))입니다. 왜냐하면 최대 scoville 길이만큼 반복해야하는데, 매 반복시, 정렬을 해주어야하기 때문입니다.

참고!
정렬 알고리즘의 시간 복잡도는 O(Nlog(N))입니다.

다른 방법이 필요합니다. 우리는 데이터 저장/삭제 시 정렬을 유지하는 자료구조를 알고 있습니다. 
맞습니다. "힙" 혹은 "우선 순위 큐"를 이용하여 문제를 해결하면 됩니다.

강사님의 알고리즘을 순서대로 표현하면 다음과 같습니다.

 

scoville을 토대로, 최소 힙을 생성하여 초기화합니다.
문제의 조건대로 scoville을 섞습니다. 아래의 반복 조건들을 만족할 때까지 다음을 반복합니다.
힙의 첫번째 요소(가장 작은 원소) first 를 꺼냅니다.
힙의 두번째 요소(두번째로 작은 원소) seond를 꺼냅니다.
문제 조건에 따라서, 힙에 first + second * 2를 저장합니다.
answer를 1 올립니다.
여기서 반복 조건들은 다음과 같습니다.

 

1. 힙이 비어있지 않아야 합니다.
2. 힙의 첫 원소가 K보다 작아야 합니다.
3. 힙에서 두 번째 원소를 꺼낼 수 있어야 합니다. 3번을 만족시키지 못하면 아무리 섞어도 힙의 가장 작은 원소가 K를 넘을 수 없습니다.
이를 코드로 표현하면 다음과 같습니다.

def solution(scoville, K):
    import heapq
    answer = 0
    # 1. 힙 생성 및 초기화
    heapq.heapify(scoville)

    # 2. 스코빌 지수 섞기
    # 반복 조건 1. 힙이 비어있지 않아야 한다.
    # 반복 조건 2. 힙의 첫 원소(가장 작은 수)가 K 보다 작아야 한다.
    # 반복 조건 3. 힙에서 두 번째 원소를 꺼낼 수 있어야 합니다. 없다면, -1을 반환합니다.
    # 2-1. 힙의 첫 번째 요소 first 꺼냄
    # 2-2. 힙의 두 번째 요소 second 꺼냄
    # 2-3. 힘에 first + second * 2 를 저장함
    # 2-4. answer를 1 증가시킴.
    # 2-5. 조건들을 만족할 때까지 1-4 반복
    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1
        
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    
    return answer

힙의 저장과 삭제 연산은 O(log(N))의 시간 복잡도를 가집니다. 
또한, 문제에서 최악의 경우, scoville 길이 N만큼 반복하기 때문에, 위 알고리즘의 시간 복잡도는 O(N * log(N))입니다. 
실제 코드를 제출하면 정확성 테스트까지 모두 통과하는 것을 확인할 수 있습니다.