https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    stacklist = [] # 크레인에서 뽑은 인형을 넣기 위한 stack
    answer = 0 #터트려서 사라진 인형 수
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                #moves = 1 j=3 이면 4를 stacklist 에 넣고 
                stacklist.append(board[j][i-1])
                # 보드에 있던 4는 0으로 만들어 준다.
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        #stacklist의 마지막에 넣은 인형과 마지막 직전에 넣은 인형이 같다면 2번 빼준다.
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2 #스택에서 2개를 뺏으니 2를 더한다.
                break    
    return answer

board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))