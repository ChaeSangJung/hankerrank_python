https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
	# 1
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

	# 2
    for i in range(n):
        for j in range(i, n):
    #3
            #down
            if i % 3 == 0:
                x += 1
                
            #right
            elif i % 3 == 1:
                y += 1
                
            #up
            elif i % 3 == 2:
                x -= 1
                y -= 1
      #4          
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer

n=4
print(solution(n))


for i in range(n 4):
    i=0
    for j in range(i 0, n 4):
        j=0
        if i 0 % 3 == 0:
            x = 0

        res[x 0][y 0] = num 1
            res = [
                ['1', 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]
            ]
        num = 2
        
        j=1
        if i 0 % 3 == 0:
            x = 1
        res[x 1][y 0] = num 2
            res = [
                [1, 0, 0, 0], 
                ['2', 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]
            ]
        num = 3

        j=2
        if i 0 % 3 == 0:
            x = 2
        res[x 2][y 0] = num 3
            res = [
                [1, 0, 0, 0], 
                [2, 0, 0, 0], 
                ['3', 0, 0, 0], 
                [0, 0, 0, 0]
            ]
        num = 4

        j=3
        if i 0 % 3 == 0:
            x = 3
        res[x 3][y 0] = num 4
            res = [
                [1, 0, 0, 0], 
                [2, 0, 0, 0], 
                [3, 0, 0, 0], 
                ['4', 0, 0, 0]
            ]
        num = 5

i=0 1,2,3,4
res = [
    ['1', 0, 0, 0], 
    ['2', 0, 0, 0], 
    ['3', 0, 0, 0], 
    ['4', 0, 0, 0]
]
i=1 5,6,7
i=2 8,9
i=3 10