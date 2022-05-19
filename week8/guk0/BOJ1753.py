# https://www.acmicpc.net/problem/1753
# 최단경로
# 다익스트라

from sys import stdin
import heapq
input = stdin.readline


def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start)) # 최소 힙이라 weight를 앞에 넣어야함. 안그러면 시간초과 남.
  distance[start] = 0   
  while queue:
    weight, node = heapq.heappop(queue)
    if distance[node] < weight:
      continue
    
    for next_node, next_weight in graph[node]:
      cost = distance[node] + next_weight
      if distance[next_node] > cost:        
        distance[next_node] = cost
        heapq.heappush(queue, (cost, next_node)) # 갱신된 next node의 weight를 넣어줌

V, E = map(int, input().split())
start = int(input()) -1 
inf = int(10e9)
graph = [[] for _ in range(V)]
distance = [inf for _ in range(V)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u-1].append([v-1, w])

dijkstra(start)

for el in distance:
  if el == inf:
    print("INF")
  else:
    print(el)