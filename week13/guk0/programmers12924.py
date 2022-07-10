# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

def solution(n):
    answer = 0
    
    total = 0
    p2 = 1
    for p1 in range(1, n+1):
        total += p1
            
        while total > n:
            total -= p2
            p2 += 1
        
        if total == n:
            answer += 1
    
    return answer