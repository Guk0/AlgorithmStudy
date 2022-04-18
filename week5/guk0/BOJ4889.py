# https://www.acmicpc.net/problem/4889
# 안정적인 문자열
# 문자열, 스택



from sys import stdin
from collections import deque

input = stdin.readline
number = 0

while True:
  number += 1
  text = input().strip()
  if "-" in text:
    break
  
  stack = deque() # "{"를 저장하는 stack
  cnt = 0

  for char in text:
    if char == "}":
      if len(stack) > 0:
        stack.pop()
      else:
        cnt += 1
        stack.append(char)
    else:
      stack.append(char)

  cnt += len(stack) // 2 # 남아있는 "{" 이 두개 이상인 경우 cnt에 2로 나눈 몫 추가

  print("{}.".format(number), cnt)
