# https://www.acmicpc.net/problem/1005
# ACM craft
# 위상정렬

from sys import stdin
from collections import deque
input = stdin.readline

def topology():
  queue = deque()
  
  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)
      dp[i] = time[i]

  while queue:
    a = queue.popleft()
    for i in graph[a]:
      in_degree[i] -= 1
      dp[i] = max(dp[a] + time[i], dp[i])
      if in_degree[i] == 0:
        queue.append(i)


T = int(input())
 
for _ in range(T):
  N, K = map(int, input().split())
  time = [0] + list(map(int, input().split()))
  graph = [[] for _ in range(N+1)]
  in_degree = [0 for _ in range(N+1)]
  dp = [0 for _ in range(N+1)]

  for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

  end = int(input())

  topology()
  print(dp[end])
