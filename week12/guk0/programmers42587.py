# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

from collections import deque

def solution(priorities, location):
    answer = 0
    arr = []
    for i in range(len(priorities)):
        arr.append([priorities[i], i])
    
    queue = deque(arr)
    ranked_queue = deque(sorted(arr[:], reverse=True))

    while queue:
        priority, index = queue.popleft()
        if priority >= ranked_queue[0][0]:
            ranked_queue.popleft()
            answer += 1
            if index == location:                
                break
        else:            
            queue.append([priority, index])
        
    return answer