https://www.hackerrank.com/challenges/grid-challenge/problem

def gridChallenge(grid):
    res = 'YES'
    newgrid = []
    
    for row in grid:
        newgrid.append(sorted(row))
        
    for ind in range(len(grid)):
        for jnd in range(ind, len(grid[0])):
            newgrid[ind][jnd], newgrid[jnd][ind] = newgrid[jnd][ind], newgrid[ind][jnd]
            
    for row in newgrid:
        if row != sorted(row):
            res = 'NO'
            break
            
    return res

def gridChallenge(arr):
    for j in range(len(arr[0])):
        for i in range(1,len(arr)):
            if arr[i][j]<arr[i-1][j]:
                return "NO"
    return "YES"
for _ in range(int(input())):
    arr = [sorted(input()) for i in range(int(input()))]
    print(gridChallenge(arr))

print('a'<'b') : True
print('a'>'b') : False