https://programmers.co.kr/learn/courses/30/lessons/77484

Counter는 
해시 가능한 객체를 세기 위한 dict 서브 클래스입니다. 
요소가 딕셔너리 키로 저장되고 개수가 딕셔너리값으로 저장되는 컬렉션입니다. 
개수는 0이나 음수를 포함하는 임의의 정숫값이 될 수 있습니다.

def solution(lottos, win_nums):
    lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    c = Counter(lottos) - Counter(win_nums)
    cnt = 6 - sum(v for k, v in c.items())
    return [lotto[cnt+c[0]], lotto[cnt]]

def solution(lottos, win_nums):
    answer = []
    corr_cnt=0
    unk_cnt=0
    for num in lottos:
        if num==0:
            unk_cnt+=1
            continue
        elif num in win_nums:
            corr_cnt+=1
    if corr_cnt+unk_cnt>1:
        answer.append(7-(corr_cnt+unk_cnt)) # 0을 포함한 최대 등수
    else:
        answer.append(6) # 하나 일치 할 때
    if corr_cnt>1:
        answer.append(7-corr_cnt) # 0을 제외한 최대 등수
    else:
        answer.append(6) # 하나 일치 할 때
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))