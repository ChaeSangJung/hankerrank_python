https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count # stage 1 1명 통과 못함 stage 1에 도달한 사람은 N-1명
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

num = 8

for stage in range(1, N:5+1 6):
    stage = 1
    if num 8 != 0:
        count 1 = stages.count(stage:1)
        result[stage 1] = count 1 / num 8 result = {1: 0.125}
        num 7 -= count 1
    stage = 2
    if num 7 != 0:
        count 3 = stages.count(stage:2)
        result[stage 2] = count 3 / num 7 result = {1: 0.125, 2: 0.42857142857142855}
        num 4 -= count 3
    stage = 3
    if num 4 != 0:
        count 2 = stages.count(stage:3)
        result[stage 3] = count 2 / num 4 result = {1: 0.125, 2: 0.42857142857142855, 3: 0.5}
        num 2 -= count 2
    stage = 4
    if num 2 != 0:
        count 1 = stages.count(stage:4)
        result[stage 4] = count 1 / num 2 result = {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5}
        num 1 -= count 1
    stage = 5
    if num 1 != 0:
        count 0 = stages.count(stage:5)
        result[stage 5] = count 0 / num 1 result = {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0}
        num 1 -= count 0
    stage = 6
    if num 1 != 0:
        count 1 = stages.count(stage:6)
        result[stage 5] = count 1 / num 1 result = {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0, 6: 1.0}
        num 0 -= count 1


score_dict = {
    'sam':23,
    'john':30,
    'mathew':29,
    'riti':27,
    'aadi':31,
    'sachin':28
}

result는 dictionary이므로 
sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다.
keys는 생략이 가능합니다.
print(sorted(score_dict))
# ['aadi', 'john', 'mathew', 'riti', 'sachin', 'sam']
거기에 lambda는 기준을 result[x]: 즉 value로 정렬한다는 뜻입니다.
그래서 key가 출력되게 됩니다.



print(sorted(score_dict.items(), key = lambda item: item[1], reverse=True))
# [('aadi', 31), ('john', 30), ('mathew', 29), ('sachin', 28), ('riti', 27), ('sam', 23)]
print(sorted(score_dict, key = lambda item: score_dict[item], reverse=True))
# ['aadi', 'john', 'mathew', 'sachin', 'riti', 'sam']