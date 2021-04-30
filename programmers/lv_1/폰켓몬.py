https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer=0
    N=len(nums)//2
    ponketmon=list(set(nums))
    if len(ponketmon)>N:
        answer=N
    else:
        answer=len(ponketmon)
    return answer