https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
        
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])
            
            # sum of the mid element
            mid = arr[i+1][j+1]
            
            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum

arr=[
  [0][0] [0][1] [0][2] [0][3] [0][4] [0][5]
  [1][0] [1][1] [1][2] [1][3] [1][4] [1][5]
  [2][0] [2][1] [2][2] [2][3] [2][4] [2][5]
  [3][0] [3][1] [3][2] [3][3] [3][4] [3][5]
  [4][0] [4][1] [4][2] [4][3] [4][4] [4][5]
  [5][0] [5][1] [5][2] [5][3] [5][4] [5][5]
]

arr[0][0],arr[0][1],arr[0][2],
arr[1][1],
arr[2][0],arr[2][1],arr[2][2]

arr[0][1],arr[0][2],arr[0][3],
arr[1][2],
arr[2][1],arr[2][2],arr[2][3]

arr[0][2],arr[0][3],arr[0][4],
arr[1][3],
arr[2][2],arr[2][3],arr[2][4]

arr[0][3],arr[0][4],arr[0][5],
arr[1][4],
arr[2][3],arr[2][4],arr[2][5]

arr[1][0],arr[1][1],arr[1][2],
arr[2][1],
arr[3][0],arr[3][1],arr[3][2]

arr[1][1],arr[1][2],arr[1][3],
arr[2][2],
arr[3][1],arr[3][2],arr[3][3]

arr[1][2],arr[1][3],arr[1][4],
arr[2][3],
arr[3][2],arr[3][3],arr[3][4]

arr[1][3],arr[1][4],arr[1][5],
arr[2][4],
arr[3][3],arr[3][4],arr[3][5]

arr[2][0],arr[2][1],arr[2][2],
arr[3][1],
arr[4][0],arr[4][1],arr[4][2]

.
.
.