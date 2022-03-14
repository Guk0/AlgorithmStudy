# https://www.acmicpc.net/problem/9657
# 돌게임3
# DP

N = int(input())
dp = ["", "SK", "CY", "SK", "SK"]

if N > 4:
  for i in range(5, N+1):
    if dp[i-4] == "SK" and dp[i-3] == "SK" and dp[i-1] == "SK":
      dp.append("CY")
    else:
      dp.append("SK")

  print(dp[N])
else:
  print(dp[N])


# 1개, 3개 또는 4

# 창영이 이기려면 dp 중 N - 상근이 외친 수 가 모두 상근이 승리한 경우여야 함

# 상근, 창영 순
# 1 상근
# 2 창영
# 3 상근
# 4 상근

# 5 상근    4 2 1
# 6 상근    5 3 2
# 7 창영    6 4 3
# 8 창영    7 4 3
