# https://www.acmicpc.net/problem/14425
# 문자열 집합


from sys import stdin

input = stdin.readline


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt = 0

for _ in range(M):
  char = input()
  if char in arr:
    cnt += 1

print(cnt)