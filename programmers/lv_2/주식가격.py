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