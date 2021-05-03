https://programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    answer = []
    
    que_prices = deque(prices)
    
    while que_prices :
        price = que_prices.popleft()
        up_time = 0
        for n in que_prices :
            up_time += 1
            if price > n :
                break
        answer.append(up_time)
        
    return answer

prices = [1, 2, 3, 2, 3]

while que_prices :
    prices = 1 
    deque([2, 3, 2, 3])
    
while que_prices :
    prices = 2 
    deque([3, 2, 3])

while que_prices :
    prices = 3 
    deque([2, 3])

while que_prices :
    prices = 2 
    deque([3])

while que_prices :
    prices = 3 
    deque([])

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

문제 지문 파악하기
이번에도, 입력을 통해서 문제를 파악해보도록 하겠습니다. 문제의 입력은 이렇습니다,

 

입력 :
prices = [1, 2, 3, 2, 3]
 

문제에서는 1초, 2초, .. 5초로 표현했지만, 저는 배열 인덱스를 맞추기 위해서 0초, 1초, ... 4초로 표현하도록 하겠습니다. 이제 0초 때, 주식 가격이 얼마나 유지되었는지를 살펴보죠,

 

0초:
가격 : prices[0] = 1
0초 이후 prices에서 1보다 떨어질 때까지의 주식 목록 : [2, 3, 2, 3]
유지 시간 : 4초
 

0초때는 그 이후로 현재 주식가격 1보다 떨어지는 주식이 없습니다. 즉 그 이후로 계속 유지 된다는 것이죠. 이제 각 초를 살펴보죠.

 

1초:
가격 : prices[1] = 2
1초 이후 prices에서 2보다 떨어질 때까지의 주식 목록 : [3, 2, 3]
유지 시간 : 3초
 

1초 때 역시, 이 이후로, 현재 가격 2보다 떨어지지 않습니다.

 

2초:
가격 : prices[2] = 3
2초 이후 prices에서 1보다 떨어질 때까지의 주식 목록 : []
유지 시간 : 1초
 

2초 떄는 현재 가격 3에서 1초 후, 3초에서 2로 떨어집니다. 그래서 유지 시간은 1초입니다.

 

3초:
가격 : prices[3] = 2
3초 이후 prices에서 1보다 큰 주식 가격 목록 : [3]
유지 시간 : 1초
 

3초때 역시, 이 이후로 떨어지지 않습니다. 남은 시간 1초간 유지됬다고 생각하면됩니다.

 

4초:
가격 : prices[4] = 3
4초 이후 prices에서 1보다 큰 주식 가격 목록 : []
유지 시간 : 0초
 

마지막 시간 4초 때는 유지 시간이 없는걸로 칩니다. 즉 0초이지요. 어떻게 풀어야 할까요?

 

저 역시 많은 고민을 해보았습니다. (사실, 그냥 푸는건 10분도 안되었는데, 스택을 이용해서 푸려니...) 그래서 저의 메인 아이디어는 이렇습니다. "시간을 스택에 쌓자!"

 

무슨 말이냐면, 먼저 0초 때 상황입니다. 이 때는 그냥 스택에 초를 저장합니다.

 

현재 시간 : 0초
st = [0]
 

이제 1초 후입니다. 먼저 현재 시간의 주식가격과 스택 st에 저장된 마지막 시간의 주식 가격을 비교합니다.

 

현재 시간 : 1초
st = [0]
prices[1] = 2 > prices[0] = 1
 

만약 현재 주식 가격이 크다면, 스택에 저장합니다.

 

현재 시간 : 1초
st = [0, 1]
 

2초 역시 1초 떄까지와 마찬가지로 현재 시간의 주식가격과 스택에 저장된 마지막 시간의 주식가격을 비교합니다. 현재 주식가격이 크군요. 따라서 스택에 그 시간을 저장합니다.

 

현재 시간 : 2초
st = [0, 1, 2] (prices[2] > prices[1])
 

3초 때를 비교해봅시다. 현재 주시가격보다, 스택에서 마지막에 저장된 시간의 주식가격이 더 큽니다.

 

현재 시간 : 3초
st = [0, 1, 2]
prices[3] = 2 < prices[2] = 3
 

이 때는, 스택에서 마지막 시간을 빼온 후, 현재 시간 - 마지막 시간, 즉 유지 시간을 구합니다. 

 

현재 시간 : 3초
st = [0, 1] //2 빠짐
answer[2] = 3 - 2 // 유지 시간
 

반복해서, 현재 시간의 주식가격과 스택에 저장된 마지막 시간의 주식가격을 비교합니다.

 

현재 시간 : 3초
st = [0, 1]
prices[3] = 2 == prices[1] = 2
 

가격이 같기 때문에, 현재 시간을 저장합니다.

 

현재 시간 : 3초
st = [0, 1, 3]
 

즉, 스택에 저장된 마지막 시간의 주식 가격이, 현재 주식 가격보다, 크다면, 주식 가격은 유지하지 못한것입니다.

 

따라서, 시간이 지날 때마다, 스택에 저장된 마지막 시간의 주식 가격이 현재 주식 가격보다 작거나 같은 가격이 나올 때까지 스택에서 빼온 후, 해당 유지 시간, "현재 - 마지막에 저장된 시간"을 answer의 마지막에 저장된 시간 위치에 저장하면 됩니다.

 

이제 4초 때입니다. 스택에서 저장된 마지막 시간의 주식 가격과, 현재 주식 가격을 비교합니다.

 

현재 시간 : 4초
st = [0, 1, 3]
prices[4] = 3 > prices[3] = 2
 

따라서, 스택에 현재 시간을 저장합니다.

 

현재 시간 : 4초
st = [0, 1, 3, 4]
 

이제 첫 시간 0초부터 마지막 시간 4초까지 유지한 숫자들이 스택에 최종적으로 남습니다. 그래서, 이제 스택에서 빼오면서, 유지 시간(최종 시간 - 저장된 시간)들을 구하면 됩니다.

 

answer[스택 저장된 시간] = 최종 시간 - 스택 저장된 시간
answer[4] = 4-4 = 0
answer[3] = 4-3 = 1
answer[1] = 4-1 = 3
answer[0] = 4-0 = 4
 

이렇게 하면 답 answer를 구할 수 있습니다.

 

answer = [4, 3, 1, 1, 0]

def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        st.append(i)
    
    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top
    
    return answer

