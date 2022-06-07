# https://www.acmicpc.net/problem/1799
# 비숍
# 백트래킹 or 이분 탐색

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current, visited):
  for el in left[current]:
    if not visited[el]:
      visited[el] = True
      if right[el] == 0 or dfs(right[el], visited):
        right[el] = current
        return True
  return False


N = int(input())
left = [[] for _ in range(N*2)]
right = [0 for _ in range(N*2)]
cnt = 0

for i in range(N):
  arr = list(map(int, input().split()))
  for j in range(N):
    if arr[j] == 1:
      left[i+j+1].append(i-j+N)

for i in range(1, N*2):
  visited = [False for _ in range(N*2)]  
  if dfs(i, visited): 
    cnt += 1

print(cnt)


# vector 
# 1 -> 5
# 2 -> 4, 6
# 3 -> 3, 5, 7
# 4 -> 2, 4, 6, 8
# 5 -> 1, 3, 5, 7, 9
# 6 -> 2, 4, 6, 8
# 7 -> 3, 5, 7
# 8 -> 4, 6
# 9 -> 5
