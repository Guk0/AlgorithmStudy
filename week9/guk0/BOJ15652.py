# https://www.acmicpc.net/problem/15652
# N과 M(4)
# 백트래킹


def dfs(current):
  if len(current) == M:
    answer.append(current)
    return
  
  for i in range(current[-1], N+1):
    dfs(current+[i])


N, M = map(int, input().split())
answer = []

for i in range(1, N+1):
  dfs([i])

for el in answer:
  print(*el)