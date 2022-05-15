# https://www.acmicpc.net/problem/7490
# 0 만들기
# 백트래킹

from sys import stdin

input = stdin.readline


def dfs(index):
  if index == N:
    total = []
    for el in formulas:
      if el[0] == " ":
        total[-1] = int(str(total[-1]) + el[1])
      else:
        total.append(int(el))
      
    if sum(total) == 0:
      answer.append("".join(formulas))
    return
  
  for i in range(3):  # 0, 1, 2   ==  +, -, " "
    formulas[index] = operator[i] + arr[index]
    dfs(index+1)
    formulas[index] = ""

T = int(input())
operator = ["+", "-", " "]

for i in range(T):
  N = int(input())
  answer = []
  arr = [str(i) for i in range(1, N+1)]
  formulas = ["" for _ in range(N)]
  formulas[0] = arr[0]

  dfs(1)
  answer.sort()
  print("\n".join(answer))
  print()
  