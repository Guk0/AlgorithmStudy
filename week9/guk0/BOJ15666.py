# https://www.acmicpc.net/problem/15666
# N과 M(12)
# 백트래킹


def dfs(current, index):
  if len(current) == M:
    if tuple(current) not in answer:
      answer.add(tuple(current))
    return

  for i in range(index, N):
    dfs(current+[arr[i]], i)



N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = set()
arr.sort()

for i in range(N):
  dfs([arr[i]], i)

for el in sorted(answer):
  print(*el)