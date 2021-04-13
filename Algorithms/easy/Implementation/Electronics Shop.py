https://www.hackerrank.com/challenges/electronics-shop/problem

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

pre_cal = 0
total = -1

for i in keyboards:
    for j in drives:
        pre_cal = i+j;
        if pre_cal <= b and pre_cal > total:
            total = pre_cal

return total