# https://www.acmicpc.net/problem/15654
# N과 M(5)
# 백트래킹

def dfs(current):
  if len(current) == M:
    answer.append(current)
    return

  for i in range(N):
    if not visited[i]:
      visited[i] = True
      dfs(current+[arr[i]])
      visited[i] = False


N, M = map(int, input().split())
answer = []
visited = [False for _ in range(N)]
arr = list(map(int, input().split()))
arr.sort()

for i in range(N):
  visited[i] = True
  dfs([arr[i]])
  visited[i] = False

for el in answer:
  print(*el)