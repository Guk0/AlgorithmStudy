# https://www.acmicpc.net/problem/12852
# 1로 만들기 2
# DP

from sys import stdin
input = stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 0

for i in range(2, N+1):
  tmp = dp[i-1]
  if i % 2 == 0:
    tmp = min(tmp, dp[i//2])

  if i % 3 == 0:
    tmp = min(tmp, dp[i//3])
  
  dp[i] = tmp + 1

cnt = dp[N]
current = N
arr = [current]
while cnt > 0:
  if current % 2 == 0 and dp[current//2] == cnt - 1:
    current = current // 2
    arr.append(current)
    cnt -= 1
    continue

  if current % 3 == 0 and dp[current//3] == cnt - 1:
    current = current // 3
    arr.append(current)
    cnt -= 1    
    continue

  if dp[current-1] == cnt - 1:
    current -= 1
    arr.append(current)
    cnt -= 1    
    continue

print(dp[N])
print(*arr)
