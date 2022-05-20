# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
# 다익스트라

# 1 -> N 까지 가는데 v1, v2를 거쳐가야함.
# 1 -> v1 까지 최단 거리 + v1 -> v2 최단거리 + v2 -> N 까지 최단거리
# 1 -> v2 까지 최단 거리 + v2 -> v1 최단거리 + v1 -> N 까지 최단거리
# 이렇게 두가지 구한 후 min

import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start):
  distance = [inf for _ in range(N+1)]
  distance[start] = 0
  queue = []
  heapq.heappush(queue, [0, start])

  while queue:
    weight, node = heapq.heappop(queue)
    if distance[node] < weight:
      continue

    for next_node, next_weight in graph[node]:
      cost = distance[node] + next_weight
      if distance[next_node] > cost:
        distance[next_node] = cost
        heapq.heappush(queue, [cost, next_node])

  return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
inf = int(10e9)

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])
  graph[b].append([a, c])

v1, v2 = map(int, input().split())

from_start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

cnt = min(from_start[v1] + from_v1[v2] + from_v2[N], from_start[v2] + from_v2[v1] + from_v1[N])
print(cnt if cnt < inf else -1)
