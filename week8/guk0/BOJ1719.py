# https://www.acmicpc.net/problem/1719
# 택배
# 플로이드-워셜

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
inf = int(10e9)
graph = [[inf for _ in range(n)] for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
    graph[b-1][a-1] = min(graph[b-1][a-1], c)
    answer[a-1][b-1] = b
    answer[b-1][a-1] = a


for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]
        answer[i][j] = answer[i][k]

for i in range(n):
  answer[i][i] = '-'
for row in answer:
  print(*row)