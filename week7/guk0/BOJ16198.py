# https://www.acmicpc.net/problem/16198
# 에너지 모으기
# 백트래킹


from sys import stdin

input = stdin.readline


def dfs(arr, sumation):
  if len(arr) == 2:
    answer.append(sumation)
    return

  for i in range(1, len(arr)-1):
    tmp_arr = arr[:]
    tmp_sum = sumation
    tmp_sum += tmp_arr[i-1] * tmp_arr[i+1]
    del tmp_arr[i]
    dfs(tmp_arr, tmp_sum)

N = int(input())
circles = list(map(int, input().split()))
answer = []

dfs(circles, 0)

print(max(answer))
