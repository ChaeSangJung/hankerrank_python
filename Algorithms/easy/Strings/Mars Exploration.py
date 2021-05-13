https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):    
    errors = 0
    compare_txt = 'SOS'
    lenth_c = len(compare_txt)
    
    for i in range(len(s)):
        if compare_txt[i%lenth_c] != s[i]:
          errors += 1
    return errors