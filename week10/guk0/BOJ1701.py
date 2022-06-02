# https://www.acmicpc.net/problem/1701
# Cubeditor
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
  
  return max(table)

string = input()
cnt = 0

for i in range(len(string)):
  sub_string = string[i:len(string)]
  cnt = max(cnt, make_table(sub_string))

print(cnt)