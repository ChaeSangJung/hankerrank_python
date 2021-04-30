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

