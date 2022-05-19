# https://www.acmicpc.net/problem/1238
# 파티
# 다익스트라

# 가는길과 오는길이 다를 수 있다.

from sys import stdin
import heapq
input = stdin.readline


def dijkstra(start):
  distance = [inf for _ in range(N+1)]
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  while queue:
    weight, node = heapq.heappop(queue)
    if distance[node] < weight:
      continue
    
    for next_node, next_weight in graph[node]:
      cost = distance[node] + next_weight
      if distance[next_node] > cost:
        distance[next_node] = cost
        heapq.heappush(queue, (cost, next_node))
  
  return distance

N, M, X = map(int, input().split())
inf = int(10e9)
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])


dist_x = dijkstra(X)
distances = [0 for _ in range(N+1)]

for i in range(1, N+1):
  if i != X:
    distances[i] = dijkstra(i)[X]

max_dist = 0
for i in range(1, N+1):
  max_dist = max(max_dist, dist_x[i] + distances[i])

print(max_dist)
