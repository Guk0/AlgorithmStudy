# https://www.acmicpc.net/problem/12919
# A와 B 2

# ABA A 빼기
# BAAB B 빼기
# ABB  이 경우의 수는 없음
# BAAA 둘 다 돌려봐야함.

from collections import deque

def solution():
  global answer
  queue = deque()
  queue.append(T)

  while queue:
    text = queue.popleft()
    if len(S) > len(text):
      continue

    if S == text:
      answer = 1
      return

    if text[0] == "A" and text[-1] == "A":
      queue.append(text[:-1])
    elif text[0] == "B" and text[-1] == "B":
      queue.append(text[::-1][:-1])
    elif text[0] == "B" and text[-1] == "A":
      queue.append(text[:-1])
      queue.append(text[::-1][:-1])


S = input()
T = input()
answer = 0
solution()
print(answer)
