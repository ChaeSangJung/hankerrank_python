https://programmers.co.kr/learn/courses/30/lessons/42587
# fast campus 강의


def solution(priorities, location):
    queue = [(i, idx) for idx, i in enumerate(priorities)] #idx = location
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == location:
                return count
                break
            else:
                queue.pop(0) 
        else:
            queue.append(queue.pop(0))


priorities = [1, 1, 9, 1, 1, 1]	
location = 0

queue = [(2, 0), (1, 1), (3, 2), (2, 3)]