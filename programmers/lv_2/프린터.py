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


문제 지문 파악하기
먼저 문제에 따르면, priorities에는 문서의 중요도별로 존재합니다. 이 때 location에 위치한 문서가 출력 순서가 어떻게 되는지 반환하면 되는 문제입니다. 어느 때와 마찬가지로 입력을 예제로 직관적으로 문제를 풀어봅시다. 첫 번째 입력입니다.

 

priorities : [2, 1, 3, 2]
location : 2
 

priorities를 인덱스별로 나타내면 다음과 같습니다.

 

priorities : [2, 1, 3, 2]
index :     [0, 1, 2, 3]
location : 2
 

우리는 index가 location, 즉 2인 문서를 뽑아내면 됩니다. 문제에 따르면, prorities에서 출력될 문서들은 자신보다 중요도가 높은 문서가 있으면, 순서 맨 뒤로 가게 됩니다.

 

따라서 현재 가장 맨 앞의 문서 priority=2, index=0인 문서는 가장 맨 뒤로 갑니다.

 

front : (priority=2, index=0)
priorities : [1, 3, 2, 2]
index :     [1, 2, 3, 0]
location : 2
 

이제 맨 앞의 문서는 priority=1, index=1인 녀석이 됩니다. 그러나 역시 prorities 안에 중요도가 높은 문서가 존재하므로, 맨 뒤로 갑니다.

 

front : (priority=1, index=1)
priorities : [3, 2, 2, 1]
index :     [2, 3, 0, 1]
location : 2
 

이제 맨 앞의 문서는 priority=3, index=2인 녀석입니다. priorities 중 자신보다 높은 중요도를 가지고 있는 문서는 존재하지 않습니다. 따라서, 이 문서를 출력하면 됩니다.

 

이 때 이 문서를 출력했을 때, 출력 횟수는 1이 됩니다. 또한, location과 idx가 일치하므로, 이 문제의 입력에 따른 답은 1이 됩니다. 어떻게 동작하는지 아시겠나요?

 

이 문제에서 "중요도"를 빼면, 선입 선출 구조로 문서가 출력된다는 것을 알 수 있습니다. 따라서 큐를 통해서 문제를 풀수 있다는 것이죠. 이번엔 큐를 이용해서 문제를 풀어봅시다. 먼저, (idx, priority) 쌍으로 저장되는 큐를 생성합니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 0 //출력 횟수
q : [ (0, 2), (1, 1), (2, 3), (3, 4) ] // (idx, proirity) 쌍으로 저장하는 큐
 

이제 큐가 비거나, location에 해당하는 문서가 출력될때까지 문서를 출력해봅시다. 먼저 처음 저장된 문서를 빼옵니다.

 

priorities : [2, 1, 3, 2]
location : 2
front : (0, 2) //빼온 문서
q : [ (1, 1), (2, 3), (3, 4) ] //문서 하나가 빠짐.
 

이 때 빼온 문서 front의 중요도보다 높은 중요도를 가진 문서가 큐에 있는지 확인합니다. (idx=2, priority=3)인 문서가 있네요. 그러면, 다시 q에 저장합니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 0
front : (0, 2)
q : [ (1, 1), (2, 3), (3, 4), (0, 2) ] //다시 들어옴.
 

다시, q에서 첫 번째 문서를 빼옵니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 0
front : (1, 1) //빼온 문서
q : [ (2, 3), (3, 4), (0, 2) ] //문서 하나가 빠짐
 

역시 front보다 중요도가 높은 문서가 q속에 존재합니다. 다시 q에 넣습니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 0
front : (1, 1)
q : [ (2, 3), (3, 4), (0, 2), (1, 1) ] //다시 들어옴
 

다시, q에서 첫 번째 문서를 빼옵니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 0
front : (2, 3) // 빼온 문서
q : [ (3, 4), (0, 2), (1, 1) ] //문서 하나가 빠짐
 

현재 문서 front보다 중요도가 높은 문서는 q속에 없습니다. 따라서, 이 문서를 출력합니다.

 

priorities : [2, 1, 3, 2]
location : 2
answer : 1 //출력해서 1올라감.
front : (2, 3)
q : [ (3, 4), (0, 2), (1, 1) ]
 

근데 현재 출력된 문서의 idx가 location의 값인 2로 일치합니다. 이 경우, 출력을 멈추가 정답을 반환하면 됩니다. 어떻게 동작하는지 보이시나요? 이제 코드를 통해서 알아봅시다.