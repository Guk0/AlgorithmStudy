# https://www.acmicpc.net/problem/12904
# A와 B
# 모든 경우의 수를 고려하는 경우는 안됨. 최대 2^999.


from collections import deque


def solution(text):
  while True:
    if S == text:
      return 1
    if len(S) > len(text):
      return 0

    if text[-1] == "A":
      text = text[:-1]
    else:
      text = text[:-1][::-1]


S = input()
T = input()
print(solution(T))


# 1 2 3 4 5 6 7
# 2 4 8 16 32

# 2^n
