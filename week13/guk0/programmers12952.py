# https://school.programmers.co.kr/learn/courses/30/lessons/12952
# N-Queen

length = 0
answer = 0

def dfs(current, previous_row, check1, check2):
    global length, answer
    if current == length:
        answer += 1
        return
    
    for i in range(length):
        if i not in previous_row and current+i not in check1 and current-i not in check2:
            dfs(current+1, previous_row+[i], check1 + [current+i], check2+[current-i])
        

def solution(n):
    global length, answer
    length = n
    
    dfs(0, [], [], [])
    
    return answer