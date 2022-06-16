# https://www.acmicpc.net/problem/6198
# 옥상 정원 꾸미기
# 스택

from sys import stdin
input = stdin.readline

N = int(input())
arr = []
stack = []
answer = 0

for _ in range(N):
  arr.append(int(input()))

for i in range(N):
  while stack and arr[stack[-1]] <= arr[i]:
    j = stack.pop()
    answer += i - j - 1

  stack.append(i)

for el in stack:
  answer += N - el - 1

print(answer)