# https://www.acmicpc.net/problem/1309
# 동물원
# dp

# dp배열 만들지 말고 변수로 저장해야 통과.
# 점화식 f(n) = 2 * f(n+1) + f(n)


#         xx
#   ox    xo     xx
# xx ox xx xo xx xo ox

# 경우의 수를 따지면 xx일 경우 다음 줄이 xx ox xo 총 세개
# xo나 ox일 경우 xx ox 혹은 xx xo로 총 두개.

# ox + xo를 x, xx를 y 로 놓으면
# x + y = f(n) 일때
# y는 직전 경우의 수인 f(n-1)과 같음. 모든 경우의 수에서 xx 발생함.
# x의 경우도 모두 한개씩 발생하며 직전 xx의 개수만큼 더 발생함. 즉 y개만큼 발생.
# f(n+1) = 2 * f(n) + y 이며 y는 f(n-1) 이므로
# f(n+1) = 2 * f(n) + f(n-1)
# f(n) = 2 * f(n-1) + f(n-2)


# 두번째 시도 : 메모리 초과. y + 2*dp[i-1] 를 9901로 나눴으면 해당 문제 발생 안했을듯.

N = int(input())

dp = [0 for _ in range(N+1)]
dp[0], dp[1] = 1, 3

for i in range(2, N+1):
  dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[N] % 9901)

# # 첫번째 시도 : 메모리 초과

# N = int(input())

# dp = [[0, 0] for _ in range(N+1)]
# dp[0] = [0, 1]

# for i in range(1, N+1):
#   previous = sum(dp[i-1])
#   dp[i][0] = previous + dp[i-1][1]
#   dp[i][1] = previous

# print(sum(dp[N]) % 9901)


# 세번째 시도

# N = int(input())
# total = 7
# x, y = 3, 7

# for i in range(2, N):
#   total = 2*y + x
#   x, y = y, total

# if N == 1:
#   print()
# else:
#   print(total % 9901)

