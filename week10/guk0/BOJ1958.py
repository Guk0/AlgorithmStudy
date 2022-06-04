# https://www.acmicpc.net/problem/1958
# LCS3

# 3차원 배열로 풀어야함
# A: dababcf
# B: ababdef
# C: df

# LCS(A,B): ababf
# LCS(LCS(A,B),C):  f     -> 2차원 배열로 2번 lcs 돌렸을때
# LCS(A,B,C): df          -> 3차원 배열로 돌렸을떄



def get_lcs(string1, string2, string3):
  lcs = [[[0 for _ in range(len(string3))] for _ in range(len(string2))] for _ in range(len(string1))]
  for i in range(1, len(string1)):
    for j in range(1, len(string2)):
      for k in range(1, len(string3)):
        if string1[i] == string2[j] == string3[k]:
          lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
        else:
          lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])

  return lcs

a = [0] + list(input())
b = [0] + list(input())
c = [0] + list(input())

lcs = get_lcs(a, b, c)

print(lcs[-1][-1][-1])

