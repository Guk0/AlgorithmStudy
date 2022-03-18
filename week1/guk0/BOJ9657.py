# https://www.acmicpc.net/problem/9657 , 9658
# 돌게임3, 4
# DP

# 돌게임 3

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


# 돌게임 4

# N = int(input())
# dp = ["", "CY", "SK", "CY", "SK"]

# if N > 4:
#   for i in range(5, N+1):
#     if dp[i-4] == "CY" or dp[i-3] == "CY" or dp[i-1] == "CY":
#       dp.append("SK")
#     else:
#       dp.append("CY")

#   print(dp[N])
# else:
#   print(dp[N])

# 상근 -> 창영 순
# 1 창영
# 2 상근
# 3 창영
# 4 상근
# 5 상근
# 6 상근



