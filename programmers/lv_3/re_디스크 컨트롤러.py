https://programmers.co.kr/learn/courses/30/lessons/42627

문제 지문 파악하기
이번에도, 입력을 통해서 문제를 파악해보도록 하겠습니다. 문제의 입력은 이렇습니다.

 

입력:
jobs = [[0, 3], [1, 9], [2, 6]]
 

이 때, 먼저 최초 작업은 request=0, expend=3인 작업을 진행합니다. 그러면 결국 이렇게 됩니다.

 

jobs = [[1, 9], [2, 6]]
n = 1 //처리한 작업의 개수
time = 3 //현재 시간 (0 + expend=3)
answer = 3 // 작업 요청부터 작업이 마무리까지 걸린 시간 (0 + expend)
 

이제 어떤 작업을 골라야 할까요? 이럴 경우, 요청 시간이 짧은 걸 먼저 처리할수록, answer에 크기가 작아집니다. 즉, request=2, expend=6인 작업을 처리합니다.

 

jobs = [[1, 9]]
n = 2 //처리한 작업의 개수
time = 9 //현재 시간 (time = 3 + expend = 6)
answer = 10 // 작업 요청부터 작업이 마무리까지 걸린 시간 (answer = 3 + time = 9 - request = 2)
 

이제 마지막 작업을 처리합니다.

 

jobs = []
n = 3 //처리한 작업의 개수
time = 18 //현재 시간
answer = 27 // 작업 요청부터 작업이 마무리까지 걸린 시간 (answer = 10 + time = 18 - request = 1)
 

그래서 이들의 평균을 구하면 됩니다.

 

answer = 9 (answer = 27 / n = 3)
 

이번엔 다른 예제를 살펴볼까요? 다음 입력이 들어왔다고 가정합시다.

 

입력:
jobs = [[1, 9], [2, 15], [10, 1]]
 

그럼 이젠 request=1, expend=9인 작업을 처리하죠?

 

jobs = [[2, 6], [10, 1]]
n = 1 //처리한 작업의 개수
time = 10 //현재 시간 (time = request = 1 + expend = 9)
answer = 9 (0 + time = 10 - request = 1)
 

이제 2가지 중 어떤 걸 처리해야 할까요? 이 때는 현재 시간 기준으로 이미 들어온 입력들이 우선순위를 가집니다. 즉 request=2, expend=6인 작업을 처리해야 합니다.

 

jobs = [[10, 1]]
n = 2 //처리한 작업의 개수
time = 16 // time = 10 + expned = 6
answeer = 23 // answer = 9 + time = 16 - request =2
 

이제 request = 10, expend = 1 인 작업을 처리합니다.

 

jobs = []
n = 3 //처리한 작업의 개수
time = 17 // time = 16 + expned = 1
answeer = 30 // answer = 23 + time = 17 - request = 10
 

여기서 나눈 몫을 구하면 답은 다음과 같습니다.

 

answer = 10 // answer = 30 / n = 3
 

어떻게 풀 수 있을까요? 먼저 이 문제는 파트 "힙"에서 알 수 있듯이 우선 순위 큐를 써야 합니다. 제가 세운 알고리즘은 다음과 같습니다. 우선, 입력은 첫 번째 입력으로 하겠습니다.

 

입력:
jobs = [[0, 3], [1, 9], [2, 6]]
 

먼저, jobs를 정렬시키고, time의 최초 시간을, jobs의 첫 원소의 요청 시간으로 설정합니다. (두 번째 경우를 위해서입니다.)

 

jobs = [[0, 3], [1, 9], [2, 6]]
time = 0
 

그리고 우선순위 큐를 하나 생성해둡니다.

 

jobs = [[0, 3], [1, 9], [2, 6]]
time = 0
pq = []
 

이제 작업들을 처리해봅시다. 먼저 첫 원소를 빼줍니다. 이때, 개수를 세워줍니다.

 

jobs = [[1, 9], [2, 6]]
(request, expend) = [0, 3]
n = 1
time = 0
pq = []
 

위에서 손으로 풀어보았을 때, 결국 time은 작업 처리할 때 다음 수식을 만족합니다.

 

time += expend

 

또한, answer는 다음 수식을 만족합니다.

 

answer += (time - request)

 

이제 작업을 처리한 시간들을 계산해줍시다.

 

jobs = [[1, 9], [2, 6]]
(request, expend) = [0, 3]
n = 1
time = 3
answer = 3
pq = []
 

그리고 현재 시간 time보다 작은 request를 가진 작업이 jobs에 있다면, 모두 뺴내 pq에 저장합니다. 대신, 이 pq는 expend 기준으로 최대 힙인 우선순위 큐로 합니다.

 

이때는 time=3이므로, [1, 9], [2, 6] 모두 뺴져 pq로 들어가게 됩니다. 들어갈 때, expend 기준으로 들어가야 합니다! 즉 이렇게 될 것입니다.

 

jobs = []
(request, expend) = [0, 3]
n = 1
time = 3
answer = 3
pq = [[9, 1], [6, 2]] //expend 기준
 

이제 우선순위 큐 pq가 빌 떄까지 다시 원소를 꺼내어, jobs에 머리에 넣습니다. 즉, pq에서 우선순위가 가장 낮은 원소가 결국은 다음에 빠져나가야할 원소인 것입니다.

 

//pq 처음 뺴낼 때
jobs = [[2, 6]]
(request, expend) = [0, 3]
n = 1
time = 3
answer = 3
pq = [[9, 1]]

//pq 처음 뺴낼 때
jobs = [[2, 6], [1, 9]]
(request, expend) = [0, 3]
n = 1
time = 3
answer = 3
pq = []
 

이제, 위의 과정을 반복합니다. 각 과정을 반복했을 때, 나타나는 결과는 다음과 같습니다. 한 번 손으로 직접 풀어보세요!

 

n = 2
jobs = [[1, 9]]
time = 9
answer = 10

n = 3
jobs = []
time = 18
answer = 27
 

jobs가 이제 비게 되면, answer를 n으로 나눈 몫을 답으로 반환하면 됩니다. 즉 이 문제에서 답은 9입니다.

구르미의 알고리즘 풀이
"문제 지문 파악하기"를 토대로 세운 알고리즘을 순서대로 나열하면 다음과 같습니다.

 

1. jobs를 정렬합니다.
2. 최초 시간 time을 정렬된 jobs[0][0]로 합니다.
3. 우선순위 큐 pq를 생성합니다. 이 때 (expend, request)를 원소로 합니다.
4. jobs가 빌 때까지 다음을 반복합니다.
    1. jobs의 첫 원소를 꺼내옵니다.
    2. n에 1을 더해줍니다.
    3. time에 꺼내온 원소의 소요 시간 expend을 더해줍니다.
    4. answer에 time에 꺼내온 원소의 요청 시간 request를 뺀 시간을 더해줍니다.
    5. jobs가 비지 않고 jobs[0][0]가 time 보다 작을 때, 다음을 반복합니다.
        1. jobs에서 원소를 꺼내옵니다.
        2. 우선순위 큐 pq에 소요 시간 기준 Max 힙으로 원소를 저장합니다.
    6. 우선순위 큐 pq가 빌 때까지 다음을 반복합니다.
        1. pq에서 원소를 꺼내옵니다.
        2. 그 원소를 다시 jobs 첫 원소로 집어넣습니다.
5. answer에 n을 나눈 몫을 저장하고 반환합니다.

이를 코드로 표현하면 다음과 같습니다.

def solution(jobs):
    import heapq

    # 1. jobs 정렬
    jobs.sort()
    answer = 0
    n = 0
    # 2. 최초 시간 설정
    time = jobs[0][0]
    # 3. 우선순위 큐 생성
    pq = []
    
    # 4. job이 빌 떄까지 다음을 반복합니다.
    while jobs:
        # 1. jobs의 첫 원소를 꺼내옵니다.
        (request, expend) = jobs.pop(0)
        # 2. n에 1을 더해줍니다.
        n += 1
        # 3. time에 소요 시간 expend를 더해줍니다.
        time += expend
        # 4. answer에 현재 시간 time에서 요청 시간 request를 뺸 값을 더해줍니다.
        answer += (time - request)
        
        # 5. jobs가 비지 않고, jobs[0][0]일 떄 다음을 반복합니다.
        while jobs and jobs[0][0] < time:
            # 1. jobs의 첫 원소를 꺼내옵니다.
            (request, expend) = jobs.pop(0)
            # 2. 해당 원소를 expend 기준으로 pq에다 저장합니다.
            heapq.heappush(pq, (-expend, request))

        # 6. pq가 빌 떄까지 다음을 반복합니다.
        while pq:
            # 1. pq에서 원소를 꺼냅니다.
            (expend, request) = heapq.heappop(pq)
            # 2. jobs에 첫 원소로 저장합니다.
            jobs.insert(0, [request, -expend])

    # 5. answer에 n을 나눠준 몫을 저장하고 반환합니다.
    answer //= n
    return answer