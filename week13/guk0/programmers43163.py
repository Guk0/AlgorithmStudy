# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환

from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, []))
    
    while queue:
        current_word, arr = queue.popleft()
        if current_word == target:
            return len(arr)
        
        for word in words:
            if word not in arr:
                cnt = 0
                for i in range(len(word)):
                    if word[i] != current_word[i]:
                        cnt += 1
                if cnt == 1:
                    queue.append((word, arr+[word]))
    return 0    

def solution(begin, target, words):    
    return bfs(begin, target, words)