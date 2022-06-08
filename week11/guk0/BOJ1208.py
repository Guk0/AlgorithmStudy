# https://www.acmicpc.net/problem/1208
# 부분수열의 합 2
# 이분탐색, 중앙에서 만나기

from sys import stdin
from itertools import combinations
input = stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

l_arr = arr[:len(arr)//2]
r_arr = arr[len(arr)//2:]

l_sums = []
r_sums = []

for i in range(len(l_arr)+1):
  for el in combinations(l_arr, i):
    l_sums.append(sum(el))

for i in range(len(r_arr)+1):
  for el in combinations(r_arr, i):
    r_sums.append(sum(el))

answer = 0

l_sums.sort()
r_sums.sort()

left = 0
right = len(r_sums) - 1
ans = 0

while left < len(l_sums) and right >= 0:
  tmp = l_sums[left] + r_sums[right]
  if tmp == S:
    same_count_left = 1
    same_count_right = 1

    same_left_idx = left
    same_right_idx = right

    left += 1
    right -= 1

    while left < len(l_sums) and l_sums[left] == l_sums[same_left_idx]:
      same_count_left += 1
      left += 1
    
    while right >= 0 and r_sums[right] == r_sums[same_right_idx]:
      same_count_right += 1
      right -= 1
    
    answer += same_count_left * same_count_right
  
  elif tmp < S:
    left += 1
  
  else:
    right -= 1

if S == 0:
  answer -= 1
    
print(answer)

