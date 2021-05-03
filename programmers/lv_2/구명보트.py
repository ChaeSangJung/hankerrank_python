https://programmers.co.kr/learn/courses/30/lessons/42885

문제 지문 파악하기
이번에도 문제의 입력을 통해서, 문제를 파악해보도록 하겠습니다. 다음은, 문제의 첫 번째 입력입니다.

people = [70, 50, 80, 50]
limit = 100

여기서 70kg인 사람을 먼저 내보낸다고 합시다. 구명 보트의 최대 무게 limit이 30kg가 빕니다. 그러나 무인도에 남은 인원 중 30kg 이하인 사람은 없습니다. 그럼 70kg인 사람 한 명만 나갑니다.

people = [50, 80, 50] // 70kg 사람 나감.
limit = 100 (100 >= 70)
answer = 1 // 필요 보트 개수

이제 50kg인 사람을 내보냅시다. 이 때 limit에 비해 구명보트는 50kg인 사람을 1명 더 태울 수 있습니다. 따라서, 50kg 2명이 이 때 나가게 됩니다.

people = [80] // 50kg x 2 사람 나감.
limit = 100 (100 >= 50 + 50)
answer = 2

이제 80kg인 사람을 한 명 내보냅니다.

people = [] // 80kg 사람 나감.
limit = 100 (100 >= 80)
answer = 3

즉 3개의 구명보트가 있어야 무인도에 있는 모든 사람들을 구할 수 있습니다. 손으로 풀면 간단하지만, 프로그래밍적으로 풀면 간단하지가 않습니다. 우리가 찾아야 할 키 포인트는 이겁니다.

보트는 최대 2명씩 탈 수 있습니다.

이 문제에서 최대한 2명씩 보트에 태우는 것이 핵심입니다. 어떻게 이렇게 내보낼 수 있을까요? 제가 세운 방안은 다음과 같습니다.

"무거운 사람"부터 나간다. "가벼운 사람"은 무거운 사람 나갈 때, 끼어들 수 있으면, 같이 나가자.

자 한번 위의 전략대로 해봅시다. 먼저 사람들을 무게가 큰 순으로 정렬시켜줍니다.

people = [80, 70, 50, 50]

제일 무거운 사람의 위치를 first, 제일 가벼운 사람의 위치를 last라고 하겠습니다.

people = [80, 70, 50, 50]
first = 0 // 제일 무거운 사람은 제일 첫 번째
last = 3 // 제일 가벼운 사람은 제일 마지막 (people 길이 -1)

이제 first의 위치한 사람을 내보냅시다. 이때, first에 위치하는 사람과 last에 위치하는 사람의 무게의 합이 limit 이하인지 확인합니다.

limit = 100
people[first] + people[last] = 130

무게의 합이 limit을 초과하므로 그냥 first만 내보냅니다. 내보낸다는 표시로 1증가시키기로 하지요.

people = [80, 70, 50, 50]
first = 1 // 80kg은 나갔다. 70이 이제 최고 몸무게
last = 3

또, first에 위치한 사람을 내보냅시다. 역시 first, last에 위치한 사람들의 무게의 합이 limit 이하인지 비교합니다.

limit = 100
people[first] + people[last] = 120

이번에도 limit을 초과합니다. first에 위치한 사람만 내보냅시다.

people = [80, 70, 50, 50]
first = 2 // 70kg은 나갔다.
last = 3

다시 first에 위치한 사람을 내보냅시다. 무게의 합을 비교합니다.

limit = 100
people[first] + people[last] = 100

이번엔 limit이하입니다. 따라서, last에 위치한 사람도 같이 나갑니다. last는 -1 하는 것이 나가는 걸로 하겠습니다.

people = [80, 70, 50, 50]
first = 3 // 세번째 위치하던 50kg 나갔습니다.
last = 2 // 마지막 위치하던 50kg 나갔습니다.

이제 모든 인원이 나갔습니다. 모든 인원이 나간 것은 다음 수식을 만족할 때입니다.

first > last

즉, first <= last가 만족할 때까지, first를 내보내되, last도 함께 나갈 수 있는지 확인하면 됩니다. 그리고 이 반복과정을

거친 first를 반환하면 됩니다.

알고리즘 풀이
"문제 지문 파악하기"를 토대로 세운 알고리즘을 순서대로 나열하면 다음과 같습니다.

1. 무거운 순으로 사람들을 정렬시킵니다.
2. 무거운 사람부터 차례대로 나가게 합니다.
    1. 이 때, 무거운 사람과 가벼운 사람의 합이 limit보다 작다면, 가벼운 사람도 같이 나갑니다.
3. 사람들이 나간 횟수를 셉니다.

이를 프로그래밍적으로 서술하면, 다음과 같습니다.

1. people을 무게 역순으로 정렬합니다.
2. 시작점 first=0, 끝점 last=n-1로 표시합니다.
3. first <= last 만족할 때까지 다음을 반복합니다.
    1. people[first] + people[last] <= limit 이라면, last 1 줄입니다.
    2. first 1늘립니다.
4. first를 반환합니다.

다음을 코드로 나타내면 다음과 같습니다.

def solution(people, limit):
    # 1. people을 정렬합니다.
    people = sorted(people, reverse=True)
    # 2. 시작점, 끝점 표시
    first, last = (0, len(people)-1)
    
    # 3. 시작점이 끝점보다, 커질 떄까지 반복
    while first <= last:
        # 1. people[first] + people[last] <= limit 이라면, last 1 줄임
        if people[first] + people[last] <= limit:
            last -= 1
        
        # 2. first 1늘림
        first += 1
    
    # 4. 시작점 반환
    answer = first
    return answer

def solution(people, limit):    
    people = sorted(people, reverse=True)
    first, last = (0, len(people)-1)

    while first <= last:    
        if people[first] + people[last] <= limit:
            last -= 1

        first += 1
    
    
    answer = first
    return answer