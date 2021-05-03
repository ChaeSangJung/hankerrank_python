https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length #다리 위에 있는 트럭
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

bridge_length=2	
weight=10	
truck_weights=[7,4,5,6]

q = [0,0]
while q:
    sec = 1
    q.pop(0), q = [0]
    if truck_weights:
        if sum(q:0)+truck_weights[0:7]<=weight:10:
            q.append(truck_weights.pop(0)) q= [0,7], truck_weights=[4,5,6]

q= [0,7]
while q:
    sec = 2
    q.pop(0), q = [7]
    if truck_weights:
        if sum(q:7)+truck_weights[0:4]<=weight:10:
        else 
            q.append(0), q = [7,0]

q = [7,0]
while q:
    sec = 3
    q.pop(0), q = [0]
    if truck_weights:
        if sum(q:0)+truck_weights[0:4]<=weight:10:
            q.append(truck_weights.pop(0)) q= [0,4], truck_weights=[5,6]

q= [0,4]
while q:
    sec = 4
    q.pop(0), q = [4]
    if truck_weights:
        if sum(q:4)+truck_weights[0:5]<=weight:10:
            q.append(truck_weights.pop(0)) q= [4,5], truck_weights=[6]

.
.
.

문제 지문 파악하기
이전과 마찬가지로, 입력을 통해서 문제를 차근히 풀어보도록 하겠습니다. 우선, 첫 번째 입력을 살펴보시죠.

 

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
 

이 경우 다리의 길이는 2, 다리를 지날 수 있는 트럭들의 최대 무게는 10입니다. 먼저, 7을 진행한다고 해보죠.

0초 때 상황은 다음과 같습니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 0
curr_weight = 0
bridge = [ ]
 

이제 1초 후인 1초 때 상황을 살펴볼까요?

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 1
curr_weight = 7
bridge = [ 7(1) ]
 

트럭이 이제 지나갑니다. 7(1)은 무게 7인 트럭이 1만큼 이동했다는 뜻입니다. 이제 그 다음 2초 때 상황을 살펴보도록 하겠습니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 2
curr_weight = 7
bridge = [ 7(2) ]
 

이 때, 다음 트럭인 무게가 4인 트럭은 지나갈 수 없습니다. 왜냐하면, 4인 트럭이 다리를 지난다고 가정했을 때, 
총 무게는 11(curr_weight(7) + 4)이므로 입력 weight보다 크기 때문입니다.

 

그리고 2초 때 7인 트럭은 다리를 모두 지나게 됩니다. 그러므로 결국, 다리에는 아무 트럭도 없게 됩니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 2
curr_weight = 0
bridge = [ ]
 

이제 그 다음 1초 후인 3초 때 상황을 살펴보겠습니다. 이제 다리에 어떤 트럭도 없기 때문에 무게가 4인 트럭이 움직입니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 3
curr_weight = 4
bridge = [ 4(1) ]
 

이제 그 다음 4초 때 상황을 살펴보도록 하겠습니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

진행 상황:
curr_time = 4
curr_weight = 9
bridge = [ 4(2), 5(1) ]
 

이 때 무게가 5인 다음 트럭이 진행해도, 입력 weight(10 > 4 + 5)보다 작기 때문에, 다리를 진행시켜도 됩니다. 
그리고 4초 때, 무게가 4인 트럭은 다리를 모두 지나게 됩니다. 따라서 4초에 최종 상황은 다음과 같습니다.

 

입력:
bridge_length = 2 
weight = 10 
truck_weights = [7,4,5,6] 

진행 상황:
curr_time = 4 
curr_weight = 5 
bridge = [ 5(1) ]
 

다음은 각 시간에 따른 다리의 진행상황입니다.

 

입력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

5초 때 진행 상황:
curr_time = 5
curr_weight = 5 -> 0 
bridge = [ 5(2) -> - ]
==========================================
6초 때 진행 상황:
curr_time = 6
curr_weight = 6
bridge = [ 6(1) ]
==========================================
7초 때 진행 상황:
curr_time = 7
curr_weight = 6 -> 0 
bridge = [ 6(2) -> - ]
==========================================
8초: 모든 트럭이 지남! 
 

8초 때 모든 트럭이 지나기 때문에, 답은 8이 됩니다.

 

어떻게 이 문제를 풀 수 있을까요? 저는 이 문제를 풀기 위해서 스택과 큐를 조합해서 문제를 풀었습니다. 
저의 아이디어는 이렇습니다. 문제를 풀기 위해서는 
현재 다리를 지나는 트럭들의 무게를 나타내는 curr_weight, truck_weights를 역순으로 초기화된 스택 st, 큐 q와 각 트럭이 진행하는 거리를 나타내는 dist가 필요합니다.

 

anwer = 0 // 현재 시간.
curr_weight = 0
st = [6, 5, 4, 7]
q = []
dist = [0,, 0, 0, 0]
 

자 이제, 첫 번째 트럭을 지나가게 해봅시다. 일단 스택에서 데이터를 뺍니다. 이것을 top이라고 합시다.

 

anwer = 1
curr_weight = 0
st = [6, 5, 4] //7 빠짐
q = []
dist = [0,, 0, 0, 0]
top = 7
 

자 이제 현재 다리를 지나는 트럭들의 무게 curr_weight와 현재 지나가야 하는 트럭 top의 합이 weight보다 큰지 확인해봅시다.

 

curr_weight(0) + top(7) < weight(10)
 

weight보다 작군요! 트럭이 나갈 수 있습니다. 이제 curr_weight에 top을 더해주고, q에 top을 넣습니다.

 

anwer = 1
curr_weight = 7
st = [6, 5, 4]
q = [ 7 ] // 7 들어옴
dist = [0,, 0, 0, 0]
top = 7
 

그 후 q의 길이만큼 dist를 순회하여, 1씩 더해줍니다.

 

anwer = 1
curr_weight = 7
st = [6, 5, 4]
q = [ 7 ]
dist = [1,, 0, 0, 0] // 거리 1 진행 top = 7
 

계속 진행시켜보죠. 2초 때 상황입니다. 먼저 st에서 다음으로 지나가야할 트럭 top을 가져오겠습니다.

 

anwer = 2
curr_weight = 7
st = [6, 5] // 4빠짐
q= [ 7 ]
dist = [1, 0, 0, 0] // 거리 1 진행
top = 4
 

이 때, 다리를 지나는 트럭들의 무게의 합 curr_weight 와 top을 더해서 weight를 초과하는지 살펴봅시다.

 

curr_weight(7) + top(4) > weight(10)
 

그럼 4인 트럭 top은 다리를 지나선 안됩니다. 다시 스택에 집어넣습니다.

 

anwer = 2
curr_weight = 7
st = [6, 5, 4] // 다시 들어옴
q = [ 7 ]
dist = [1, 0, 0, 0] 
top = -
 

이제, 다리에 올라와 있는 트럭들을 진행시킵니다.

 

anwer = 2
curr_weight = 7
st = [6, 5, 4] // 다시 들어옴
q = [ 7 ]
dist = [2, 0, 0, 0] // 거리 1
진행 top = -
 

이 때, dist 맨 앞의 원소, 즉 가장 앞선 트럭이 진행한 거리가 bridge_length 에 도달했는지 확인합니다.

 

dist[0](2) == bridge_length(2)
 

도달했네요. 그럼 q와 dist에서 첫 원소를 빼줍니다. 이것이 트럭이 지난걸로 치는 겁니다. 첫 트럭이 다리를 지났으니 curr_weight도 그 무게만큼 빼줘야 합니다.

 

anwer = 2
curr_weight = 0 // 트럭 빠짐
st = [6, 5, 4]
q = [ ] // 트럭 빠짐
dist = [ 0, 0, 0] // 트럭 빠짐
top = -
 

이렇게 계속 진행하면 됩니다. 다음은 이후에 나타나는 각 상황입니다.

 

3초 때:
anwer = 3
curr_weight = 4
st = [6, 5]
q = [4]
dist = [1, 0, 0]
top = 4
========================
4초 때:
anwer = 4
curr_weight = 5
st = [6]
q = [5]
dist = [1, 0]
top = 5
========================
5초 때:
anwer = 5
curr_weight = 0
st = [6]
q = []
dist = [0]
top = -
========================
6초 때:
anwer = 6
curr_weight = 6
st = []
q = [6]
dist = [1]
top = -
 

이 때, 마지막 트럭이 다리를 지나는 순간은 6초입니다. 그리고 마지막 트럭이 다리를 지나는 순간을 구하는 과정은 결국 "스택"에 모든 데이터가 사라졌을 경우를 뜻합니다.

 

이후에는 위의 과정을 무시하고, 마지막 트럭이 남은 거리 + 1을 asnwer에 더해주면 됩니다. 왜냐하면, 문제에서 "마지막 트럭이 다리를 모두 지나는 순간"을 구하는 것이기 때문에, 큐에 데이터가 얼마나 있던 나머지 데이터들은 필요가 없기 때문입니다. 그럼 답을 구하도록 하겠습니다.

 

length = dist의 가장 마지막 데이터 = 1
answer = answer + (bridge_length - length + 1) = 6 + 2 - 1 + 1 = 8
 

어떻게 동작하는지 아시겠나요? 이제 코드를 살펴보도록 합시다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr_weight = 0
    # 1. 스택 생성
    st = truck_weights[::-1]
    # 2. 큐 생성
    q = []
    # 3. 진행 거리 배열 생성
    dist = [0] * len(truck_weights)
    # 4. 마지막 트럭이 다리를 지날때까지 다음을 반복합니다.
    while st:
        # 1. 출발해야 할 트럭 top을 구합니다. 즉, st에서 데이터를 빼옵니다.
        top = st.pop()
        
        # 2. 현재 다리를 지나는 트럭들의 무게와, top의 무게를 더한 값이 weight보다 큰지 확인 합니다.
        # 2-1. 크다면, 현재 트럭은 다리를 지나지 않습니다. 다시 스택으로 되돌립니다.
        # 2-2. 그렇지 않다면, 트럭은 다리를 지납니다. 즉 큐에 데이터를 넣고 다리를 지나는 트럭의 무게를 더합니다.
        if curr_weight + top > weight:
            st.append(top)
        else:
            curr_weight += top
            q.append(top)
            
        # 3. 현재 다리에 들어선 트럭들을 움직입니다. 즉, 각 진행 거리를 나타내는 dist를 q의 길이만큼 순회하여 1씩 더해줍니다.
        for i in range(len(q)):
            dist[i] += 1
        
        # 4. 다리를 지난 트럭을 제거합니다. 진행 거리가, 입력 bridge_length보다 큰지 확인합니다.
        # 4-1. curr_weight에서 q의 첫 원소만큼 빼주고, q에서 그 데이터를 제거합니다.
        # 4-2. dist 역시 첫 원소를 제거해주어야 합니다.
        if dist[0] >= bridge_length:
            curr_weight -= q.pop(0)
            dist.pop(0)
        
        answer += 1
    
    # 5. 마지막 트럭의 진행한 거리를 구합니다.
    length = dist.pop()
    # 6. answer 에 마지막 트럭이 다리를 지나는 시간 (다리 길이 - 현재 진행한 길이 + 1)을 더합니다.
    answer += (bridge_length - length + 1)
    return answer