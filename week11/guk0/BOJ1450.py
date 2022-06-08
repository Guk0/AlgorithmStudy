# https://www.acmicpc.net/problem/1450
# 냅색 문제
# 이분탐색, 중앙에서 만나기

from math import floor
from sys import stdin
from itertools import combinations
input = stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

l_arr = arr[:len(arr)//2]
r_arr = arr[len(arr)//2:]
len_l_arr = len(l_arr)
len_r_arr = len(r_arr)

l_sums = []
r_sums = []

for i in range(len_l_arr+1):
  for el in combinations(l_arr, i):
    l_sums.append(sum(el))

for i in range(len_r_arr+1):
  for el in combinations(r_arr, i):
    r_sums.append(sum(el))


l_sums.sort()
answer = 0

for r_el in r_sums:
  if r_el > C:
    continue

  left = 0
  right = len(l_sums)

  while left < right:
    mid = floor((left + right) / 2)
    if r_el + l_sums[mid] > C:
      right = mid
    else:
      left = mid + 1

  answer += right

print(answer)