# https://www.acmicpc.net/problem/1325
# 효율적인 해킹


from sys import stdin
from collections import deque

def bfs(start): 
  cnt = 1 
  visited = [0 for _ in range(N+1)] 
  visited[start] = 1 
  queue = deque([start]) 
  while queue: 
    u = queue.popleft() 
    for v in graph[u]: 
      if not visited[v]: 
        queue.append(v) 
        visited[v] = 1 
        cnt += 1 
  return cnt


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[b].append(a)

results = []
max_cnt = 0

for i in range(1, len(graph)):
  cnt = bfs(i) 
  if cnt >= max_cnt: 
    max_cnt = cnt 
    results.append([i, cnt])

for i, cnt in results:
  if cnt == max_cnt:
    print(i, end=' ')