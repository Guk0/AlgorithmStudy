# https://www.acmicpc.net/problem/1766
# 문제집
# 위상 정렬

from sys import stdin
import heapq
input = stdin.readline

def topology_sort():
  queue = []
  for i in range(1, N+1):
    if in_degree[i] == 0:
      heapq.heappush(queue, i)

  while queue:
    node = heapq.heappop(queue)
    result.append(node)
    for next_node in graph[node]:
      in_degree[next_node] -= 1
      if in_degree[next_node] == 0:
        heapq.heappush(queue, next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
result = []

for _ in range(M):
  first, second = map(int, input().split())
  graph[first].append(second)
  in_degree[second] += 1

topology_sort()

print(*result)