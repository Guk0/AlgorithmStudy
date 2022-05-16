# https://www.acmicpc.net/problem/9663
# N-Queen


def dfs(current):
  global answer
  if current == N:
    answer += 1
    return
  
  for i in range(N):
    if not row[i] and not diagonal_l[current+i] and not diagonal_r[current-i+N-1]:
      row[i], diagonal_l[current+i], diagonal_r[current-i+N-1] = True, True, True
      dfs(current+1)
      row[i], diagonal_l[current+i], diagonal_r[current-i+N-1] = False, False, False


N = int(input())
row = [False for _ in range(N)]
diagonal_l = [False for _ in range(N*2-1)] # 대각선 저장
diagonal_r = [False for _ in range(N*2-1)]

answer = 0
dfs(0)
print(answer)