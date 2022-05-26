# https://www.acmicpc.net/problem/15663
# N과 M(9)
# 백트래킹

# not current in answer 에서 시간 초과
# set과 tuple이용하여 해결(set에는 list가 들어갈 수 없음)

def dfs(current):
  if len(current) == M:
    if tuple(current) not in answer:
      answer.add(tuple(current))
    return

  for i in range(N):
    if not visited[i]:
      visited[i] = True
      dfs(current + [arr[i]])
      visited[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(N)]
answer = set()
arr.sort()


for i in range(N):
  visited[i] = True
  dfs([arr[i]])
  visited[i] = False

for el in sorted(answer):
  print(*el)


