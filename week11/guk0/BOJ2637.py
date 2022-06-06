# https://www.acmicpc.net/problem/2637
# 장난감 조립
# 위상 정렬

from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
  queue = deque()
  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)
      dp[i] = 1

  while queue:
    node = queue.popleft()
    for next_node, cnt in graph[node]:
      dp[next_node] += (dp[node] * cnt)
      in_degree[next_node] -= 1
      if in_degree[next_node] == 0:
        queue.append(next_node)


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
middle = set()

for i in range(M):
  X, Y, K = map(int, input().split())
  graph[X].append([Y, K])
  in_degree[Y] += 1
  middle.add(X)

topology_sort()

for i in range(1, N+1):
  if i not in middle:
    print(i, dp[i])

# 문제의 조건을 역으로 뒤집어서 완제품 -> 기본부품 순으로 가야함.


