# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

from collections import deque
import heapq


def solution(jobs):    
    answer = 0
    jobs_len = len(jobs)
    jobs.sort()
    jobs = deque(jobs)
    queue = []    
    current = 0
    while queue or jobs:
        if not queue:
            start, duration = jobs.popleft()
            current = start # 모든 큐가 비고 다시 원소가 추가될 경우 current를 start로 조정해야함.
            heapq.heappush(queue, [duration, start])
        
        duration, start = heapq.heappop(queue)
        answer += current-start + duration
        current += duration
            
        while jobs and jobs[0][0] < current:
            next_start, next_duration = jobs.popleft()
            heapq.heappush(queue, [next_duration, next_start])
    
        print(answer)
    
    return answer // jobs_len