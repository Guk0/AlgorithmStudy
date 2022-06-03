# https://www.acmicpc.net/problem/16172
# 나는 친구가 적다 (Large)
# KMP

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

def kmp(string1, string2):
  table = make_table(string2)
  j = 0

  for i in range(len(string1)):
    if 48 <= ord(string1[i]) <= 57:
      continue

    while j > 0 and string1[i] != string2[j]:
      j = table[j-1]

    if string1[i] == string2[j]:
      if j == len(string2) - 1:
        return(1)
      else:
        j += 1
  
  return(0)


S = input()
K = input()
print(kmp(S, K))