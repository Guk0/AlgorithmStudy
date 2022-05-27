# https://www.acmicpc.net/problem/14502
# 연구소


from sys import stdin
from itertools import combinations
from collections import deque
import copy

input = stdin.readline


def bfs(graph):
  global answer
  queue = deque(viruses)
  dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
        graph[ny][nx] = 2
        queue.append([ny, nx])
  
  cnt = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        cnt += 1

  answer = max(answer, cnt)
  

N, M = map(int, input().split())
graph = []
empties = []
viruses = []
answer = 0

for i in range(N):
  row = list(map(int, input().split()))
  graph.append(row)
  for j in range(len(row)):
    if row[j] == 2:
      viruses.append([i, j])
    
    if row[j] == 0:
      empties.append([i, j])

combis = combinations(empties, 3)

for el in combis:
  for coordinate in el:
    graph[coordinate[0]][coordinate[1]] = 1

  tmp_graph = copy.deepcopy(graph)
  bfs(tmp_graph)

  for coordinate in el:
    graph[coordinate[0]][coordinate[1]] = 0

print(answer)