https://www.hackerrank.com/challenges/repeated-string/problem

answer = 0

s_num = len(s)
value_num = n//s_num
mod_num = n%s_num

s_mod = s[:mod_num:]

a_in_s = len(list(filter(lambda x: x == "a", s)))
a_in_s_mod = len(list(filter(lambda x: x == "a", s_mod)))

if s_num == 0:
    answer = 0
elif s_num == 1 and s=="a":
    answer == n
elif s_num == 1 and s!="a":
    answer = 0

answer = value_num*a_in_s + a_in_s_mod

return answer

 1   2   3      value_num = n 10 //s_num 3 3
aba/aba/aba/"a"

ab/ab/ab/ab/ab  mod_num = n 10 %s_num 2 0  s_mod = s[:mod_num 0:] []
aba/aba/aba/"a" mod_num = n 10 %s_num 3 1  s_mod = s[:mod_num 1:] ["a"] 
abaa/abaa/"ab"  mod_num = n 10 %s_num 4 2  s_mod = s[:mod_num 2:] ["a","b"] 
abaaba/"abab"   mod_num = n 10 %s_num 6 4  s_mod = s[:mod_num 4:] ["a","b","a","b"] 
