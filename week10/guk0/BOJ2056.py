# https://www.acmicpc.net/problem/2056
# 작업
# 위상정렬

from sys import stdin
from collections import deque
input = stdin.readline


def topology_sort():
  queue = deque()
  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)
      dp[i] = max(dp[i-1], times[i])

  while queue:
    node = queue.popleft()
    for next_node in graph[node]:
      dp[next_node] = max(dp[node] + times[next_node], dp[next_node])
      in_degree[next_node] -= 1
      if in_degree[next_node] == 0:
        queue.append(next_node)

N = int(input())
times = [0]
graph = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]

for i in range(1, N+1):
  time, cnt, *nodes  = map(int, input().split())
  times.append(time)
  in_degree[i] += cnt
  for node in nodes:    
    graph[node].append(i)

topology_sort()
print(max(dp))
