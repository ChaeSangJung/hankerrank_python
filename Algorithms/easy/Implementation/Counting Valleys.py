https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    # Write your code here
    cnt = 0
    in_vally = "no"
    lat = 0

    for step in path:
        if step == "U":
          lat += 1
        elif step == "D":
          lat -= 1
        
        if lat < 0 and in_vally == "no":
            in_vally = "yes"
        
        if lat == 0 and in_vally == "yes":
            in_vally = "no"
            cnt += 1
    
    return cnt

path=["D","D","U","U","U","U","D","D"]

cnt = 0
in_vally = "no"
lat = 0

                 / \
 __            /     \ __
     \       /
        \  /
     D  D  U U U U D D
lat -1 -2 -1 0 1 2 1 0
     y  -  - n - - - - 
cnt          1