# https://www.acmicpc.net/problem/1254
# 팰린드롬 만들기


char = input()

for i in range(len(char)):
  if char[i:] == char[i:][::-1]:
    print(len(char)+i)
    break
