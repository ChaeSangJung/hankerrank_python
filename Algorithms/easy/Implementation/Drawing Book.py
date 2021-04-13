https://www.hackerrank.com/challenges/drawing-book/problem

n=10
p=3

total_page = 1+n//2 
# 1:1, 2:2,3 3:4,5 .... 6:10,11

view_page = 1+p//2
# 3을 보려면 2page

result = 0

# 1 2/3 4/5 6/7 8/9 10/11
# 1  2  '3'  4   5    6
#      2   3

forward_page = view_page - 1
backward_page = total_page - view_page

if forward_page > backward_page:
    result = backward_page
elif forward_page < backward_page:
    result = forward_page

return result