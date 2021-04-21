https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    # commands에 있는 command(i, j, k)를 뽑는다.
    for command in commands:

        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j] # array에서 슬라이스를 하고

        slice.sort() # 정렬하고

        answer.append(slice[k-1]) # 인덱싱하자

    return answer

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))