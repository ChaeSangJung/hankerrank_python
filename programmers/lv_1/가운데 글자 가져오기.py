https://programmers.co.kr/learn/courses/30/lessons/12903
참고 https://velog.io/@joy/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B0%80%EC%9A%B4%EB%8D%B0-%EA%B8%80%EC%9E%90-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0

def solution(s):
	if len(s) % 2 == 1:
		return s[len(s)//2]
	else:
		return s[(len(s)//2-1) : (len(s)//2+1)]