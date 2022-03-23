# https://www.acmicpc.net/problem/1753
# 최단경로
# 다익스트라

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
start = int(input())

distance = [1e9 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for _ in range(E):
  u, v, w = map(int, input().split()) # u: 시작 노드, v: 끝 노드, w: u~v의 가중치
  graph[u].append([v, w])


def djikstra(start):
  queue = []
  heapq.heappush(queue, [0, start])
  distance[start] = 0

  while queue:
    dist, node = heapq.heappop(queue) # dist: 1에서부터 거리. node: graph의 index

    if distance[node] < dist:
      continue

    for el in graph[node]:
      end, weight = el[0], el[1]
      cost = distance[node] + weight
      if cost < distance[end]:
        distance[end] = cost
        heapq.heappush(queue, [cost, end])

djikstra(start)

for i in range(1, V+1):
  if distance[i] == 1e9:
    print("INF")
  else:
    print(distance[i])
