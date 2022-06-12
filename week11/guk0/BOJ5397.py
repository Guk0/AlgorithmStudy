# https://www.acmicpc.net/problem/5397
# 키로거

from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
  string = input().strip()

  cursor_stack = []
  stack = []
  
  for i in range(len(string)):
    if string[i] == "<":
      if stack:
        cursor_stack.append(stack.pop())
      continue

    if string[i] == ">":
      if cursor_stack:
        stack.append(cursor_stack.pop())
      continue
    
    if string[i] == "-":
      if stack:
        stack.pop()
      continue
    
    stack.append(string[i])

  while cursor_stack:
    stack.append(cursor_stack.pop())
  
  print("".join(stack))
  