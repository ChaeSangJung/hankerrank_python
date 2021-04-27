https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]


while len(progresses):3> 0:
    if (progresses[0,93] + time,0*speeds[0,1] : 93) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 1
    
    if (progresses[0,93] + time,1*speeds[0,1] : 94) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 2
    
    if (progresses[0,93] + time,2*speeds[0,1] : 95) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 3
    
    if (progresses[0,93] + time,3*speeds[0,1] : 96) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 4

    if (progresses[0,93] + time,4*speeds[0,1] : 97) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 5

    if (progresses[0,93] + time,5*speeds[0,1] : 98) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 6
    
    if (progresses[0,93] + time,6*speeds[0,1] : 99) >= 100:
    else:
      if count,0 > 0:  False
      time += 1 : time = 7

    if (progresses[0,93] + time,7*speeds[0,1] : 100) >= 100:
        progresses.pop(0)    progresses = [30, 55]
        speeds.pop(0)        speeds = [30, 5]
        count += 1           count = 1

while len(progresses):2> 0:
    if (progresses[0,30] + time,7*speeds[0,30] : 100) >= 100:
        progresses.pop(0)    progresses = [55]
        speeds.pop(0)        speeds = [5]
        count += 1           count = 2
.
.
.