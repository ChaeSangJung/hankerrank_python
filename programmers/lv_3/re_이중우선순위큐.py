https://programmers.co.kr/learn/courses/30/lessons/42628
https://gurumee92.tistory.com/174?category=782306

문제 지문 파악하기
이번에도, 입력을 통해서 문제를 파악해보도록 하겠습니다. 문제의 입력은 이렇습니다.

입력:
operations = ["I 16","D 1"]

이제 차례 차례 operations를 보고 이중 우선순위 큐에 데이터를 넣어봅시다. 먼저 첫번 째입니다. 해당 문자열을 " " 기준으로 자릅니다.

elem = "I 16"
op = "I"
num = 16

이제 우선순위 큐에 16을 저장합니다.

pq = [ 16 ]

이제 다음 데이터를 봅시다. 데이터는 이렇게 될 겁니다.

elem = "D 1"
op = "D"
num = 1
pq = [ 16 ]

이제 D에 1이 나왔으니 우선순위 큐 최댓값을 제거합니다.

pq = [] // 최댓값 제거

모든 데이터를 돌았습니다. 우선순위 큐가 비었을 때는 0,0 을 반환합니다.

answer = [0, 0]

이제 다른 입력을 살펴보도록 하겠습니다.

입력: operations = ["I 7","I 5","I -5","D -1"]

자 순회해봅시다. 다음은 operations를 순회할때마다 데이터 상황입니다. 한 번 손으로 직접 풀어보시고 비교해보세요.

첫 번째:
elem = "I 7"
op = "I"
num = 7
pq = [ 7 ] // 7 삽입

두 번째:
elem = "I 5"
op = "I"
num = 5
pq = [ 7, 5 ] //5 삽입

세 번째:
elem = "I -5"
op = "I"
num = -5
pq = [ 7, 5, -5 ] //-5 삽입

네 번째:
elem = "D -1"
op = "D"
num = -1
pq = [ 7, 5 ] // 최솟값 -5 삭제

따라서, 현재 pq에 저장된 최댓값, 최솟값을 반환하면 됩니다.

answer = [7, 5]

이제 이 문제를 어떻게 풀 수 있을까요? 이 문제는 문제 자체에 힌트가 있습니다. "이중 우선 순위 큐"! 즉, 우선 순위 큐 2개를 이용하여, 풀 수 있습니다. 이번엔, 다음 입력이 들어온다고 가정해봅시다.

입력:
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

먼저, 우선순위 큐 2개를 생성해둡니다. 둘 다, 우선순위가 최대값이 높은 MAX 힙 기반의 우선순위 큐입니다.

pq1 = []
pq2 = []

이제 operations를 순회합니다.

elem = "I -45"
op = "I"
num = -45

우선순위 큐 pq1이 메인입니다. -45를 pq1에 저장합니다. 데이터 상황은 이렇습니다.

elem = "I -45"
op = "I"
num = -45
pq1 = [-45]
pq2 = []

계속 진행해보겠습니다. 두 번째 상황입니다.

elem = "I 653"
op = "I"
num = 653
pq1 = [653, -45] // 653 삽입, 최대 힙 우선순위 큐임을 잊지마세요.
pq2 = []

이제 세 번째 상황입니다.

elem = "D 1"
op = "D"
num = 1

이때, 최댓값을 삭제해야 합니다. pq1에서 바로 삭제하면 됩니다. 결국 세번째 상황에서 데이터들을 다음과 같습니다.

elem = "D 1"
op = "D"
num = 1
pq1 = [-45] // 최댓값 653 제거
pq2 = []

이제 설명이 필요한 상황, 최솟값을 제거하는 상황이 나올때까지 설명을 건너뛰겠습니다. 대신, 각 상황의 데이터만 표시하도록 하죠.

네 번째 상황:
elem = "I -642"
op = "I"
num = -642
pq1 = [-45, -642]
pq2 = []

다섯 번째 상황:
elem = "I 45"
op = "I"
num = 45
pq1 = [45, -45, -642]
pq2 = []

여섯 번째 상황:
elem = "I 97"
op = "I"
num = 97
pq1 = [97, 45, -45, -642]
pq2 = []

일곱 번째 상황:
elem = "D 1"
op = "D"
num = 1
pq1 = [45, -45, -632]
pq2 = []

자 이제 여덟 번째 상황에서 문자열은 다음과 같습니다.

elem = "D -1"
op = "D"
num = -1

이제 우선순위 큐 pq1에서 최솟값을 삭제해야 합니다. 어떻게 할 수 있을까요? 우선순위 큐 pq1은 Max 힙입니다. 즉, 첫 원소가 가장 큰 데이터이며, 마지막 원소가 가장 적은 데이터를 저장합니다. 따라서, 마지막 원소를 제외한 모든 원소를 pq2에 옮겨놓습니다.

pq1 = [-632]
pq2 = [45, -45]

이제 pq1에서 최솟값을 제거합니다.

pq1 = []
pq2 = [45, -45]

그 후, 다시 pq2의 모든 원소를 pq1으로 옮겨 놓습니다.

pq1 = [45, -45]
pq2 = []

결국 여덟 번째 상황의 데이터 값은 다음과 같습니다.

elem = "D -1"
op = "D"
num = -1
pq1 = [45, -45] //최솟값 -632 제거
pq2 = []

그 후 마지막 상황은 다음과 같습니다.

elem = "I 333"
op = "I"
num = 333
pq1 = [333, 45, -45]
pq2 = []

이제 pq1의 최댓값, 최솟값을 answer에 순서대로 넣으면 됩니다. 기억하세요! 최댓값은 pq1의 첫 번째 원소, 최솟값은 pq1의 마지막 원소입니다. 즉 답은 다음과 같습니다.

answer = { 333, -45 }

만약 모든 연산을 순회했을 때, pq1이 비어있다면, 0, 0을 반환하시면 됩니다.

알고리즘 풀이

"문제 지문 파악하기"를 토대로 세운 알고리즘을 순서대로 나열하면 다음과 같습니다.

1. 우선순위 큐 2개를 생성합니다.
2. operations를 다음과 같이 순회합니다.
    1. 순회 문자열 elem을 연산자와 숫자로 나누어 자릅니다. ("OP" + " " + "NUM")
    2. 만약 연산자가 I라면, 우선순위 큐 pq1에 num을 집어넣습니다.
    3. 만약 연산자가 D일 때, 우선순위 큐 pq1가 비어있다면 넘어갑니다.
    4. 만약 연산자가 D, 우선순위 큐 pq1에 원소가 있을 때, num이 1이라면, 우선순위 큐 pq1에서 데이터를 빼냅니다.
    5. 만약 연산자가 D, 우선순위 큐 pq1에 원소가 있을 때 num이 -1이라면, 최솟값을 빼내야 합니다.
        1. 우선순위 큐 pq1에서 원소 1개가 남을 때까지, 원소를 모두 빼내어 다른 우선순위 큐 pq2에 임시 저장합니다.
        2. 마지막 원소 최솟값을 우선순위 큐 pq1에서 꺼냅니다.
        3. pq2의 모든 원소를 다시 pq1으로 이동시킵니다.
3. 이렇게 초기화된 우선순위 큐 pq1이 비어있다면, answer 에 0, 0을 넣고 반환합니다.
4. 이렇게 초기화된 우선순위 큐 pq1에 데이터가 있다면, answer에 최댓값, 최솟값을 넣고 반환합니다.
    1. 최댓값은 우선순위 큐 pq1의 첫 원소입니다.
    2. 최솟값은 우선순위 큐 pq1의 마지막 원소입니다.

def solution(operations):
    import heapq

    # 1. 우선순위 큐 생성
    pq = []
    
    # 2. operations 순회
    for operate in operations:
        # 1. 문자열 " " 기준으로 연산자, 숫자를 나눔
        (op, num) = operate.split(" ")
        num = int(num)

        # 2. 연산자가 I 라면 우선순위 큐에 num 저장
        if op == 'I':
            heapq.heappush(pq, num)
            continue
        
        # 3. 연산자 D일 때 pq가 비었다면, 연산 X
        if not pq:
            continue
        
        # 4. -1이라면 최솟값 제거, 힙 연산 이용
        if num == -1:
            heapq.heappop(pq)
        # 5. 1이라면, 최댓값 제거, 슬라이스 연산 이용
        else:
            pq.remove(max(pq))

    # 3. 최댓값, 최솟값 구해서 반환
    answer = [max(pq), min(pq)] if pq else [0, 0]
    return answer

from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]