# https://www.acmicpc.net/problem/1041
# 주사위
# 그리디

# sum1
# ABC ABD AED AEC FBC FBD FED FEC
# 012 013 034 024 125 135 345 245
# 8개 중 min

# sum2
# AB AC AD AE FD FB FC FE BD BC CE DE
# 01 02 03 04 35 15 25 45 13 12 24 34
# 12개 중 min

# 윗면에서 양 모서리 sum1, 가장자리(모서리 제외) sum2, 나머지 sum3
# 나머지 양 모서리 sum2, 가장자리 sum3

# 3일때
# 24 + 12 + 1 윗면
# 12 + 4      중간
# 12 + 4      아래

# 37 + 32


N = int(input())
arr = list(map(int, input().split()))

if N > 1:
  sum1 = min(
    arr[0]+arr[1]+arr[2], arr[0]+arr[1]+arr[3], 
    arr[0]+arr[3]+arr[4], arr[0]+arr[2]+arr[4], 
    arr[1]+arr[2]+arr[5], arr[1]+arr[3]+arr[5], 
    arr[3]+arr[4]+arr[5], arr[2]+arr[4]+arr[5]
  )
  sum2 = min(
    arr[0]+arr[1], arr[0]+arr[2], arr[0]+arr[3], arr[0]+arr[4],
    arr[4]+arr[5], arr[3]+arr[5], arr[2]+arr[5], arr[1]+arr[5],
    arr[1]+arr[2], arr[1]+arr[3], arr[3]+arr[4], arr[2]+arr[4]
  )
  sum3 = min(arr)

  upper_edge = sum1 * 4
  upper_border = sum2 * (N-2) * 4
  upper_etc = sum3 * (N**2 - 4 - ((N-2) * 4))
  middle_edge = 0
  middle_border = 0
  for _ in range(N-1):
    middle_edge += sum2 * 4
    middle_border += sum3 * (N-2) * 4

  print(upper_edge+upper_border+upper_etc+middle_edge+middle_border)

else:
  print(sum(arr)-max(arr))




# 위 min값을 구하는 과정을 아래와 같이 단순화 시킬 수 있음.
# ABCDEF 중 [0, 5], [1, 4], [2, 3] 3개의 최소값을 구해서 
# 모서리일땐 3개 최소값 더해서 사용
# border일땐 3개 중 최소 2개 값 더해서 사용
# 나머지 일땐 3개 중 최소값 구해서 사용
