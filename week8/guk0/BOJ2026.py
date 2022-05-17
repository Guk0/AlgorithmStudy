# https://www.acmicpc.net/problem/2026
# 소풍
# 백트래킹

# 1->12->123->1236 한글자씩 붙여서 계속 체크하면 1은 결국 나머지 236에서 전부 체크함.


from sys import stdin

input = stdin.readline

def check(idx, friends):
  for number in friends:
    if not graph[idx][number]:
      return False
  return True

def dfs(idx, friends):
  if len(friends) == K:
    for char in friends:
      print(char+1)
    exit(0)

  for next_idx in range(idx+1, N):
    if graph[idx][next_idx] and cnts[next_idx] >= K-1 and not visited[next_idx] and check(next_idx, friends):
      visited[next_idx] = True
      dfs(next_idx, friends + [next_idx])
      visited[next_idx] = False

K, N, F = map(int, input().split())
graph = [[False for _ in range(N)] for _ in range(N)]
cnts = [0 for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(F):
  a, b = map(int, input().split())
  graph[a-1][b-1] = True
  graph[b-1][a-1] = True
  cnts[a-1] += 1
  cnts[b-1] += 1

for i in range(N):
  if cnts[i] >= K-1:
    visited[i] = True
    dfs(i, [i])
    visited[i] = False

print(-1)