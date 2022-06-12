# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)    
    
    while scoville:
        food1 = heapq.heappop(scoville)
        if food1 >= K:
            break
        
        if scoville:
            food2 = heapq.heappop(scoville)
            heapq.heappush(scoville, food1+food2*2)
            answer += 1
        else:
            return -1
    
    return answer

