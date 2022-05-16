# https://www.acmicpc.net/problem/1613
# 역사
# 플로이드-워셜

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
graph = [[False for _ in range(n)] for _ in range(n)]

for _ in range(k):
  a, b = map(int, input().split())
  graph[a-1][b-1] = True


for t in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue

      if not graph[i][j] and graph[i][t] and graph[t][j]:
        graph[i][j] = True

s = int(input())


for _ in range(s):
  a, b = map(int, input().split())

  if graph[a-1][b-1]:
    print(-1)
  else:
    if graph[b-1][a-1]:
      print(1)
    else:
      print(0)