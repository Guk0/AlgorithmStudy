# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
# 다익스트라

import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start):
  distance = [inf for _ in range(N+1)]
  distance[start] = 0
  queue = []
  heapq.heappush(queue, [0, start])

  while queue:
    dist, node = heapq.heappop(queue)

    if distance[node] < dist:
      continue
    
    for el in graph[node]:
      end, weight = el[0], el[1]
      cost = distance[node] + weight
      if cost < distance[end]:
        distance[end] = cost
        heapq.heappush(queue, [cost, end])
  return distance


inf = int(10e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())
distance = dijkstra(start)
print(distance[end])

