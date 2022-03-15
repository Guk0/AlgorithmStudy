# https://www.acmicpc.net/problem/14501
# 퇴사
# dp


from sys import stdin

N = int(stdin.readline())
arr = []

for _ in range(N):
  arr.append(list(map(int, stdin.readline().split())))

dp = [0] * (N+1)
dp[N-1] = arr[N-1][1] if arr[N-1][0] == 1 else 0

for i in range(len(arr)-2, -1, -1):
  time, score = arr[i] 
  if i + time <= N:
    dp[i] = max(score + dp[i+time], dp[i+1])
  else:
    dp[i] = dp[i+1]

print(dp[0])