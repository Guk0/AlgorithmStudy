# https://www.acmicpc.net/problem/1167
# 트리의 지름


import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(idx, current_weight):
  for target, weight in graph[idx]:
    if distance[target] == -1:
      distance[target] = current_weight + weight
      dfs(target, current_weight + weight)

V = int(input())
graph = [[] for _ in range(V)]

for i in range(V):
  a, *b, c = map(int, input().split())
  for i in range(0, len(b), 2):
    graph[a-1].append([b[i]-1, b[i+1]])

distance = [-1 for _ in range(V)]
distance[0] = 0
dfs(0, 0)

next_idx = distance.index(max(distance))
distance = [-1 for _ in range(V)]
distance[next_idx] = 0
dfs(next_idx, 0)

print(max(distance))
