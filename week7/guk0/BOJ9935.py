# https://www.acmicpc.net/problem/9935
# 문자열 폭발
# 스택, 문자열


string = input()
target = input()
stack = []


for char in string:
  stack.append(char)

  if char == target[-1] and "".join(stack[-len(target):]) == target:
    del stack[-len(target):]


if len(stack) > 0:
  print("".join(stack))
else:
  print("FRULA")