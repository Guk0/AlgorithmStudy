
# https://www.acmicpc.net/problem/17212
# 달나라 토끼를 위한 구매대금 지불 도우미
# dp


N = int(input())
coin = [7, 5, 2, 1]
dp = [float("inf")] * (N+1)
dp[0] = 0

for i in range(1, N+1):
  for j in coin:
    if i >= j and dp[i-j] < dp[i]:
      dp[i] = dp[i-j] + 1

print(dp[N])
# print(dp)


# 개선

# from sys import stdin

# N = int(stdin.readline())
# coins = [1, 2, 5, 7]

# dp = [1e9] * (N + 1)
# dp[0] = 0

# for coin in coins:
#   for i in range(coin, N+1):
#     dp[i] = min(dp[i], dp[i-coin] + 1)

# print(dp[N])
