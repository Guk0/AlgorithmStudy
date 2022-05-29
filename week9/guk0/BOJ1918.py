# https://www.acmicpc.net/problem/1918
# 후위 표기식
# 스택

string = input()
operators = set(["+", "-", "*", "/", "(", ")"])
stack = []
result = ""

for char in string:
  if char not in operators:
    result += char
  else:
    if char == "(":
      stack.append(char)
    elif char in ["*", "/"]:
      while len(stack) != 0 and (stack[-1] == "*" or stack[-1] == "/"):
        result += stack.pop()
      stack.append(char)
    elif char in ["+", "-"]:
      while len(stack) != 0 and stack[-1] != "(":
        result += stack.pop()
      stack.append(char)
    elif char == ")":
      while len(stack) != 0 and stack[-1] != "(":
        result += stack.pop()
      stack.pop()

while len(stack) != 0:
  result += stack.pop()

print(result)