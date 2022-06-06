# https://programmers.co.kr/learn/courses/30/lessons/67258
# 보석쇼핑

from collections import deque

def solution(gems):
    uniq_gem = set(gems)
    gem_len = len(uniq_gem)
    dict = {gem: 0 for gem in uniq_gem}
    
    p1 = 0
    p2 = 1
    cnt = 0
    queue = deque()
    result = []
    
    for gem in gems:                         
        queue.append(gem)
        if dict[gem] == 0:
            cnt += 1            
        dict[gem] += 1
        p1 += 1
        
        while queue and dict[queue[0]] > 1:            
            dict[queue.popleft()] -= 1
            p2 += 1

        if cnt == gem_len:
            result.append([p1-p2+1, [p2, p1]])
        
    result.sort(key=lambda x: x[0])
    return result[0][1]

# ["dia", "ruby", "ruby", "emerald", "dia", "emerald"] -> [3, 5]
# ["dia", "ruby", "ruby", "emerald", "emerald", "ruby", "dia"] -> [5, 7]