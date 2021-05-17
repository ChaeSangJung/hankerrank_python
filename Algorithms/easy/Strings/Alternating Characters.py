https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    # Write your code here
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1

    return deletions


# Your task is to change it into a string such that there are no matching adjacent characters.
# 당신의 임무는 일치하는 인접한 문자가 없도록 문자열로 변경하는 것입니다.