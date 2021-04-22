https://programmers.co.kr/learn/courses/30/lessons/67256

def cal_dist(num, now_l, now_r,handed):
    # 번호 좌표화
    pos = {
        1:(0, 0), 2:(0, 1), 3:(0, 2),
        4:(1, 0), 5:(1, 1), 6:(1, 2),
        7:(2, 0), 8:(2, 1), 9:(2, 2),
        '*':(3, 0), 0:(3, 1), '#':(3, 2)
    }

    X, Y = 0, 1
    dist_l = abs(pos[now_l][X] - pos[num][X]) + abs(pos[now_l][Y] - pos[num][Y])
    dist_r = abs(pos[now_r][X] - pos[num][X]) + abs(pos[now_r][Y] - pos[num][Y])
    # 거리가 같으면
    if dist_l == dist_r:
        return 'R' if handed == 'right' else 'L'
    return 'R' if dist_l > dist_r else 'L'

def solution(numbers, hand):
    # 왼손잡이인지 오른손잡이인지
    HANDED = hand
    
    # 왼쪽 숫자, 오른쪽 숫자
    left, right = [1,4,7], [3,6,9]
    # 손 위치 초기화
    now_l, now_r = '*', '#'
    # solution
    result = ''
    for num in numbers:
        if num in left: # 왼쪽 키라인
            result += 'L'
            now_l = num
        elif num in right: # 오른쪽 키라인
            result += 'R'
            now_r = num
        else: # 중간 키라인
            result += cal_dist(num, now_l, now_r, HANDED)
            if result[-1] == 'L':
                now_l = num
            else :
                now_r = num
    
    return result

각 좌표의 거리 차이 구하기!

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"

HANDED = hand:"right"

for num in numbers:
    num = 1
        result = 'L'
        now_l = 1
    num = 3
        result = L'R'
        now_r = 3
    num = 4
        result = LR'L'
        now_l = 4
    num = 5
        cal_dist()
            dist_l:1 = abs(pos[now_l:4][X:0]:1 - pos[num:5][X:0]:1):0 + abs(pos[now_l:4][Y:1]:0 - pos[num:5][Y:1]:1):1
            dist_r:2 = abs(pos[now_r:3][X:0]:0 - pos[num:5][X:0]:1):1 + abs(pos[now_r:3][Y:1]:2 - pos[num:5][Y:1]:1):1
            return L
        result = LRL'L'
        if result[-1] == 'L':
        now_l = 5
    num = 8
    num = 2
    num = 1 
    num = 4
    num = 5
    num = 9
    num = 5
    .
    .
    .