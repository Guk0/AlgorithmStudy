# https://www.acmicpc.net/problem/4354
# 문자열 제곱
# KMP

from sys import stdin
input = stdin.readline

def make_table(string):
  table = [0 for _ in range(len(string))]
  j = 0

  for i in range(1, len(string)):
    while j > 0 and string[i] != string[j]:
      j = table[j-1]

    if string[i] == string[j]:
      j += 1
      table[i] = j

  return table


while True:
  string = input().strip()
  if string == ".":
    break

  table = make_table(string)
  if len(string) % (len(string) - table[-1]) != 0:
      print(1)
  else:
      print(len(string) // (len(string) - table[-1]))


# abcd
# [0, 0, 0, 0]

# aaaa
# [0, 1, 2, 3]

# ababab
# [0, 0, 1, 2, 3, 4]

# abcababababab
# [0, 0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

# bbabbab
# [0, 1, 0, 1, 2, 3, 4]