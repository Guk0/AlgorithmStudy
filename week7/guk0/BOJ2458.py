# https://www.acmicpc.net/problem/2458
# 키 순서
# 플로이드-워셜


from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
graph = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1][b-1] = True


for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        continue

      if not graph[i][j] and graph[i][k] and graph[k][j]:
        graph[i][j] = True


cnt_arr = [0 for _ in range(N)]
for i in range(N):
  for j in range(N):
    if graph[i][j]:
      cnt_arr[i] += 1
      cnt_arr[j] += 1

cnt = 0
for i in range(N):
  if cnt_arr[i] == N-1:
    cnt += 1

print(cnt)