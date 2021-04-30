https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    from itertools import permutations

    lst=list(permutations(numbers,2))

    set_lst=[]
    for i in lst:        
        set_lst.append(i[0]+i[1])

    result=list(set(set_lst))
    result.sort()
    
    return result