# https://www.acmicpc.net/problem/1956
# 운동
# 플로이드-워셜

from sys import stdin

input = stdin.readline

V, E = map(int, input().split())
inf = int(10e9)
graph = [[inf for _ in range(V)] for _ in range(V)]

for i in range(V):
  graph[i][i] = 0

for i in range(E):
  a, b, c = map(int, input().split())
  graph[a-1][b-1] = c


for k in range(V):
  for i in range(V):
    for j in range(V):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = inf
for i in range(V):
  for j in range(V):
    if i == j:
      continue

    if graph[i][j] != inf and graph[j][i] != inf:
      answer = min(answer, graph[i][j] + graph[j][i])

print(-1 if answer == inf else answer)