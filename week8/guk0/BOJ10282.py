# https://www.acmicpc.net/problem/10282
# 해킹
# 다익스트라

from sys import stdin
import heapq
input = stdin.readline

def djikstra(start):
  distance = [inf for _ in range(n+1)]
  distance[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))
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


T = int(input())
for _ in range(T):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  inf = int(10e9)
  
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append([a, s])

  distance = djikstra(c)
  time = 0
  cnt = 0
  for el in distance:
    if el != inf:
      cnt += 1
      time = max(time, el)
  print(cnt, time)
