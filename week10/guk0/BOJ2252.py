# https://www.acmicpc.net/problem/2252
# 줄 세우기
# 위상정렬


from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
  queue = deque()

  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)

  while queue:
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
      in_degree[next_node] -= 1
      if in_degree[next_node] == 0:
        queue.append(next_node)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
result = []

for _ in range(M):
  tall, small = map(int, input().split())
  graph[tall].append(small)
  in_degree[small] += 1

topology_sort()
print(*result)