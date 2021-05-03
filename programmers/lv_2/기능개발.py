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

문제 지문 파악하기
이전과 마찬가지로, 입력을 통해서 문제를 차근히 풀어보도록 하겠습니다. 우선, 문제의 입력을 살펴보시죠.

 

입력:
progresses = [93,30,55]
speeds = [1,30,5]
 

이제 1일이 지났다고 합시다. 그럼 각 기능의 진행 상황을 진행 속도만큼 작업이 이루어집니다. 그러면 상태는 다음과 같습니다.

 

1일 차:
progresses = [94,60,60] (progress[i] += speeds[i])
speeds = [1,30,5]
 

계속해서 반복합니다.

 

2일 차:
progresses = [95,90,65] (progress[i] += speeds[i])
speeds = [1,30,5]

3일 차:
progresses = [96,120,70] (progress[i] += speeds[i])
speeds = [1,30,5]
 

이 때, 2번째 기능은 완성되었습니다. 그러나 문제에 따르면, 이전 기능, 그러니까 먼저 들어온 첫 번째 기능이 마무리 될 때까지 배포될 수 없습니다. 따라서 계속 남습니다. 계속 진행해보죠.

 

4일 차:
progresses = [97,120,75] (progress[i] += speeds[i])
speeds = [1,30,5]

5일 차:
progresses = [98,150,80] (progress[i] += speeds[i])
speeds = [1,30,5]

6일 차:
progresses = [99,180,85] (progress[i] += speeds[i])
speeds = [1,30,5]

7일 차:
progresses = [100,210,90] (progress[i] += speeds[i])
speeds = [1,30,5]
 

이제 드디어 첫 번째 기능이 완성되었습니다. 이 순간 progresses에는 2개의 기능이 모두 완성되어서 배포시킬 수 있습니다. 이 때, answer에 2개를 넣어주면 됩니다.

 

7일 차:
progresses = [90] //완성된 기능 배포
speeds = [5] //완성된 기능 배포
answer = [2] //배포된 기능 개수를 넣어줌
 

이제 마지막 남은 기능이 완성될때까지 진행해봅시다.

 

8일 차:
progresses = [95]
speeds = [5]
answer = [2]

9일 차:
progresses = [100]
speeds = [5]
answer = [2]
 

9일이 되어서야, 세 번째 기능이 완성됩니다. 이 때 배포를 진행하면 다음과 같이 됩니다.

 

9일 차:
progresses = [] //완성된 기능 배포
speeds = [] //완성된 기능 배포
answer = [2, 1] //배포된 기능 개수를 넣어줌
 

그래서 답은 [2, 1]이 됩니다. 이 문제는 결국 들어온 순서대로 나가기 때문에, 큐로 푸는 문제입니다. 여기서 progresses, speeds를 모두 큐로 가정하고 풀면 편합니다.

def solution(progresses, speeds):
    answer = []
    
    # 1. 모든 기능이 배포될 때까지 반복
    while progresses:
        
        # 1. 각 기능들의 그 날 진행률을 더해줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        # 2. 완성된 기능이 있으면 배포함
        cnt = 0
        # 진행 상황이 100 이상이면, 배포 가능함. 이 때, 배포할 때 progresses, speeds 모두 제거해야 함.
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        # 3. 배포 개수가 1개라도 있으면, answer에 넣어줌
        if cnt > 0:
            answer.append(cnt)
            
    return answer