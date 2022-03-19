# https://www.acmicpc.net/problem/4781
# 사탕 가게
# pypy3로 통과. python3로 통과한 사람이 없음

from sys import stdin


while True:
  N, M = map(float, stdin.readline().split()) # N : 테스트케이스, M : 예산
  N, M = int(N), int(M*100 + 0.5)
  if N == 0 and M == 0:
    break
  
  dp = [0 for _ in range(M+1)]

  for _ in range(N):
    calorie, price = map(float, stdin.readline().split())
    calorie, price = int(calorie), int(price*100 + 0.5)
    for j in range(price, M+1):
      dp[j] = max(dp[j], dp[j-price] + calorie)

  print(dp[M])