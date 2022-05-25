# https://www.acmicpc.net/problem/15657
# N과 M(8)
# 백트래킹

def dfs(current, index):
  if len(current) == M:
    answer.append(current)
    return

  for i in range(index, N):
    dfs(current+[arr[i]], i)


N, M = map(int, input().split())
answer = []
arr = list(map(int, input().split()))
arr.sort()

for i in range(N):
  dfs([arr[i]], i)

for el in answer:
  print(*el)