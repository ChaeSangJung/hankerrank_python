https://programmers.co.kr/learn/courses/30/lessons/42862

# 문제를 보면 양 옆에 빌려준다.
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

_reserve : [1]
_lost : [3]

강사님의 알고리즘 풀이
강사님은 2가지 방식을 제시하고 있습니다. 
먼저 첫 번째 방식은 입력 "N의 크기가 30 이하"라는 것에 착안하여, 
먼저 초기화한 후 진행하는 방식입니다. 알고리즘의 순서는 다음과 같습니다.

먼저 N+2 크기의 배열 u을 만들고 모두 1로 초기화합니다.
reserve를 순회하여 존재하는 원소를 u의 인덱스로 하여 +1을 해줍니다.
lost를 순회하여 존재하는 원소를 u의 인덱스로 하여 -1을 해줍니다.
u를 1 <= i < N+1 범위만큼 순회합니다.
만약 u[i-1] == 0 && u[i] == 2 인 경우, 체육복을 나눠줍니다.
1의 조건이 아니고 u[i] == 2 && u[i+1] == 0 인 경우 체육복을 나눠줍니다.
값이 0인 원소, 즉 체육복이 없는 학생의 수를 구하고 n에 빼줍니다.
왜 N+2 인 공간을 생성할까요? 
그것은 배열 인덱스와 학생 번호를 맞추는 것과 동시에, 모든 요소를 접근할 때 같은 방식으로 접근하게 하기 위함입니다. 
만약 N 크기만큼 배열을 만들었다면, 4번 과정을 진행할 때, 처음과 끝에 존재하는 인덱스인지를 검사해야 합니다. 
위 알고리즘을 토대로 만든 코드는 다음과 같습니다.

def solution(n, lost, reserve):
    u = [1] * (n + 2)

    for i in reserve:
        u[i] += 1

    for i in lost:
        u[i] -= 1

    for i in range(1, n+1):
        if u[i-1] < 1 and u[i] > 1:
            u[i-1:i+1] = [1, 1]
        elif u[i] > 1 and u[i+1] < 1:
            u[i:i+2] = [1, 1]

    answer = n - len([e for e in u[1:-1] if e < 1]) 
    return answer

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)

    answer = n - len(l)        
    return answer