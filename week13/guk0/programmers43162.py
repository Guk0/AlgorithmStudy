# https://programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크

def dfs(target):
    global visited, graph
    
    for el in graph[target]:
        if not visited[el]:
            visited[el] = True
            dfs(el)
    
    return
    
    

def solution(n, computers):
    global visited, graph
    answer = 0    
    visited = [False for _ in range(n)]
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)

        
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    
    return answer