# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 하노이 탑

answer = []

def sort(block_num, start, to, mid):
    global answer
    
    if block_num == 1:
        answer.append([start, to])
        return 
    
    sort(block_num-1, start, mid, to)
    answer.append([start, to])
    sort(block_num-1, mid, to, start)

def solution(n):
    global answer
    sort(n, 1, 3, 2)
    return answer
