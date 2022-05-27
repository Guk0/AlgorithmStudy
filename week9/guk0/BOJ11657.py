# https://www.acmicpc.net/problem/11657
# 타임머신
# 벨만 포드

inf = int(10e9)
N, M = map(int, input().split())
edges = []

for _ in range(M):
  s, e, w = map(int, input().split())
  edges.append([s, e, w])

def bf(start):
  distance = [inf] * (N + 1)
  distance[start] = 0
  for i in range(1, N+1):
    for s, e, w in edges:
      if distance[s] != inf and distance[e] > distance[s] + w:
        if i == N:
          return -1
        distance[e] = distance[s] + w

  return distance

answer = bf(1)

if answer == -1:
  print(-1)
else:
  for i in range(2, N+1):
    if answer[i] == inf:
      print(-1)
    else:
      print(answer[i])
