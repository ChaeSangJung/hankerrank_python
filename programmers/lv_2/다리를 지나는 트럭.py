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