# https://www.acmicpc.net/problem/9252
# LCS2

a = [0] + list(input().strip())
b = [0] + list(input().strip())

lcs = [[0 for _ in range(len(b))] for _ in range(len(a))]
for i in range(1, len(a)):
  for j in range(1, len(b)):
    if a[i] == b[j]:
      lcs[i][j] = lcs[i-1][j-1]+1
    else:
      lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

lcs_len = lcs[-1][-1]
print(lcs_len)

if lcs_len > 0:
  y = len(a)-1
  x = len(b)-1
  result = []

  while True:
    if lcs[y][x] == 0:
      break

    if lcs[y-1][x] == lcs[y][x]:
      y -= 1
    elif lcs[y][x-1] == lcs[y][x]:
      x -= 1
    else:
      result.append(a[y])
      y -= 1
      x -= 1

  print("".join(reversed(result)))
