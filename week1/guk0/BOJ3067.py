# https://www.acmicpc.net/problem/3067
# Coins


from sys import stdin

T = int(stdin.readline())


for _ in range(T):
  N = int(stdin.readline())

  coins = list(map(int, stdin.readline().split()))
  target = int(stdin.readline())
  
  dp = [0 for _ in range(target+1)]
  dp[0] = 1 # index 0 만 1로 놓는다.

  for coin in coins:
    for j in range(coin, target + 1):
      dp[j] += dp[j-coin]

  print(dp[target])



