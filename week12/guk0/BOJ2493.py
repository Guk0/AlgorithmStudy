# https://www.acmicpc.net/problem/2493
# 탑

from sys import stdin

input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N-1, -1, -1):
  while stack and arr[i] >= arr[stack[-1]]:
    j = stack.pop()
    answer[j] = i+1

  stack.append(i)

print(*answer)