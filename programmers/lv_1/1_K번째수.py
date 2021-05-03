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

문제 지문 파악하기
이번에도, 입력을 통해서 문제를 파악해보도록 하겠습니다. 문제의 입력은 이렇습니다.

 

입력 :
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
 

이제 commands에서 하나씩 꺼내서, 시작점, 끝점, 반환할 인덱스를 가져오겠습니다.

 

command = [2, 5, 3] //commands[0]
start = 2
end = 5
idx = 3
 

문제에 따르면, 인덱스가 0부터가 아닌 1로 되어 있습니다. 이를 조정해주어야 합니다.

 

command = [2, 5, 3]
start = 1 //인덱스 조정
end = 5
idx = 2 //인덱스 조정
 

즉, 인덱스가 0부터 시작하도록 start, idx를 1씩 줄여주어야 합니다. end는 안줄여도 됩니다. 왜냐하면, 보통 언어에서 vector, slice등을 잘라낼 때 start <= x < end 의 범위로 잘라내게 됩니다. 계속 진행해보도록 하죠. 이제 start 부터 end까지 array에서 잘라냅니다.

 

command = [2, 5, 3]
start = 1
end = 5
idx = 2
sub = [5, 2, 6, 3] // array[1:5] (1 <= x <5 범위를 자름)
 

이 sub를 오름차순으로 정렬합니다.

 

command = [2, 5, 3]
start = 1
end = 5
idx = 2
sub = [2, 3, 5, 6] //오름차순 정렬
 

여기서 idx에 해당하는 5를 answer에 넣어주면 됩니다.

 

command = [2, 5, 3]
start = 1
end = 5
idx = 2
sub = [2, 3, 5, 6]
answer = [5] //sub[idx]
 

이것을 commands를 모두 순회할 때까지 반복하면 됩니다. 다음은 이후 상황에서 벌어질 데이터들의 상황입니다.

 

두 번째:
command = [4, 4, 1]
start = 3
end = 4
idx = 0
sub = [6]
answer = [5, 6]

세 번째:
command = [1, 7, 3]
start = 0
end = 7
idx = 2
sub = [1, 2, 3, 4, 5, 6, 7]
answer = [5, 6, 3]