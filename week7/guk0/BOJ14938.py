# https://www.acmicpc.net/problem/14938
# 서강그라운드
# 플로이드-워셜


from sys import stdin

input = stdin.readline

n, m, r = map(int, input().split())
inf = int(10e9)
items = list(map(int, input().split()))
graph = [[inf for _ in range(n)] for _ in range(n)]

for i in range(n):
  graph[i][i] = 0

for _ in range(r):
  a, b, l = map(int, input().split())
  graph[a-1][b-1] = l
  graph[b-1][a-1] = l


for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(n):
  sumation = 0
  for j in range(n):
    if graph[i][j] <= m:
      sumation += items[j]
  
  answer = max(answer, sumation)

print(answer)