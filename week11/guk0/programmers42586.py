# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

from collections import deque
from math import ceil
import heapq
def solution(progresses, speeds):
    progress_queue = deque(progresses)
    speed_queue = deque(speeds)
    answer = []
    time = 0
    
    while progress_queue:        
        progress = progress_queue.popleft()
        speed = speed_queue.popleft() 
        time = ceil((100 - progress) / speed)
        cnt = 1
        while progress_queue and speed_queue and progress_queue[0] + speed_queue[0] * time >= 100:
            progress_queue.popleft()
            speed_queue.popleft()
            cnt += 1
        
        answer.append(cnt)
        
    
    return answer