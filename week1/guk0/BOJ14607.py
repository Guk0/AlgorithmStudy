# https://www.acmicpc.net/problem/14607
# 피자 (Large)
# DP
# N * (N-1) // 2 vs int(N * (N-1) / 2)

N = int(input())

print(N * (N-1) // 2)


# 메모리 초과 10**9
# N = int(input())

# dp = [0, 0]

# for i in range(2, N+1):
#   dp.append((i-1 + dp[i-1]))

# print(dp[N])


# 시간초과
# import math

# N = int(input())

# dp = [0, 0]

# for i in range(2, N+1):
#   dp.append(i//2 * math.ceil(i/2) + dp[i//2] + dp[math.ceil(i/2)])

# print(dp[N])





# 0, 1, 3, 6, 10, 15,
# 1  2  3  4  5   6
# n(n-1) / 2