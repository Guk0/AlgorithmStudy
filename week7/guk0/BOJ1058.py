# https://www.acmicpc.net/problem/1058
# 친구
# 플로이드-워셜

from sys import stdin

input = stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
answer = [[0 for _ in range(N)]  for _ in range(N)]


for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j:
        continue

      if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
        answer[i][j] = 1

print(max(map(sum, answer)))


