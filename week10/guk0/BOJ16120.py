# https://www.acmicpc.net/problem/16120
# PPAP
# 스택

string = input()
stack = []
ppap = ["P", "P", "A", "P"]

for i in range(len(string)):  
  stack.append(string[i])
  stack_len = len(stack)
  while stack_len > 3 and stack[stack_len-4:stack_len] == ppap:
    del stack[stack_len-4:stack_len]
    stack.append("P")
  

if stack == ["P"]:
  print("PPAP")
else:
  print("NP")