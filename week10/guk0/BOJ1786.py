# https://www.acmicpc.net/problem/1786
# 찾기
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
  cnt = 0
  indexes = []
  j = 0

  for i in range(len(string1)):
    while j > 0 and string1[i] != string2[j]:
      j = table[j-1]

    if string1[i] == string2[j]:
      if j == len(string2) - 1:
        cnt += 1
        indexes.append(i+1 - len(string2) + 1)
        j = table[j]
        # j = table[j] 조건 없다면 아래와 같이 구간이 겹치는 케이스를 찾을 수 없음.
        # AXAXXAXX
        # AXAXX
        # table이 [0, 0, 1, 2, 0] 이 나옴. 즉 마지막 인덱스는 겹치는 친구가 없다는 것.
        # AXAX 였다면 j = 2가 돼서 뒤 AX부터 다시 검색했을 것.
        # AXAXXAXX
        #   AXAX   요런식으로
      else:
        j += 1
  
  return cnt, indexes

T = input()
P = input()
cnt, indexes = kmp(T, P)

print(cnt)
print(*indexes)
