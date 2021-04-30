https://programmers.co.kr/learn/courses/30/lessons/12906
참고 https://dojang.io/mod/page/view.php?id=2208 (슬라이싱)


def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b

def no_continuous(s):
    a = []
    for i in s:        
        if a[-1:] == [i]: continue #a[-1:] 맨 끝에 있는 것부터 끝까지
        a.append(i)    
    return a