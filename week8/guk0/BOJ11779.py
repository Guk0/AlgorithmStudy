# https://www.acmicpc.net/problem/11779
# 최소비용 구하기 2
# 다익스트라

import heapq
from sys import stdin
input = stdin.readline


def dijkstra(start):
  distance = [inf for _ in range(n+1)]
  visited = [[] for _ in range(n+1)]
  distance[start] = 0  
  queue = []
  heapq.heappush(queue, (0, start, [start])) # queue에 같이 넣어줘야 함.
  while queue:
    weight, node, path = heapq.heappop(queue)
    if distance[node] < weight:
      continue
    for next_node, next_weight in graph[node]:
      cost = distance[node] + next_weight
      if distance[next_node] > cost:
        distance[next_node] = cost
        visited[next_node] = path + [next_node]
        heapq.heappush(queue, (cost, next_node, visited[next_node]))

  return distance, visited

n = int(input())
m = int(input())
inf = int(10e9)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])

start, end = map(int, input().split())

distance, visited = dijkstra(start)
print(distance[end])
print(len(visited[end]))
print(" ".join(map(str, visited[end])))