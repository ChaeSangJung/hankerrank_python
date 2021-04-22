https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return   quicksort(more)+ equal +quicksort(less)

def solution(n):
    n = str(n)
    new = []
    for i in n :
        new.append(int(i))
    result = quicksort(new)

    answer = ''
    for i in result :
        answer += str(i)
    return int(answer)

# list에 중복일 경우
equal = []
for a in x:
    if a < pivot:
        less.append(a)
    elif a > pivot:
        more.append(a)
    else: # 중복일 경우
        equal.append(a)