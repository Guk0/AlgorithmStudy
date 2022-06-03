# https://www.acmicpc.net/problem/1305
# 광고
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

L = int(input())
string = input()
table = make_table(string)

print(L - table[L-1])



# abcab
# 3
# [0, 0, 0, 1, 2]

# bcab
# 4
# [0, 0, 0, 1]

# abcd
# 4
# [0, 0, 0, 0]

# abab
# 2
# [0, 0, 1, 2]

# ababc [0, 0, 1, 2, 0] -> 5
# cabab [0, 0, 0, 0, 0] -> 5
# bcbcc [0, 0, 1, 2, 0]  -> 5
# ccbcc [0, 1, 0, 1, 2]  -> 3
# abababcc [0, 0, 1, 2, 3, 4, 0, 0] -> 8