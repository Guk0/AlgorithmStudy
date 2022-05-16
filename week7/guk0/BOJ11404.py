# https://www.acmicpc.net/problem/11404
# 플로이드
# 플로이드-워셜


from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
inf = int(10e10)
graph = [[inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a-1][b-1] = min(graph[a-1][b-1], c)


for k in range(N):
  for i in range(N):
    for j in range(N):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
  

for i in range(N):
  for j in range(N):
    if i == j or graph[i][j] == inf:
      graph[i][j] = 0
    
for el in graph:
  print(" ".join(map(str, el)))