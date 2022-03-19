# https://www.acmicpc.net/problem/1106
# 호텔


# 유치 고객 목표치를 달성하기 위한 최소 비용
# 3/5, 1/1로 투자할 수 있다면 이를 횟수 제한 없이 여러번 사용 가능.

from sys import stdin

N, M = map(int, stdin.readline().split()) # N : 유치해야하는 고객, M: 도시수
inf = 1e9

arr = [list(map(int, stdin.readline().split())) for _ in range(M)] # 비용, 고객수

dp = [inf for _ in range(N + 101)]
dp[0] = 0

for money, customer in arr:
  for j in range(customer, N+101):
    dp[j] = min(dp[j], dp[j-customer] + money)

print(min(dp[N:]))

