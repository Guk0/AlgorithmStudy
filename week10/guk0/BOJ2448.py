# https://www.acmicpc.net/problem/2448
# 별 찍기 - 11


# N = 3, 6, 12, 24, 48

def draw_stars(current, line):
  if current == 3:
    result[line-3] += "*"
    result[line-2] += "* *"
    result[line-1] += "*****"
    return

  draw_stars(current//2, line - current//2)
  draw_stars(current//2, line)
  draw_empties(current//2, line)
  draw_stars(current//2, line)

def draw_empties(current, line):
  floor_cnt = (current // 3)*5 + (current // 3)-1
  for i in range(current):
    count = floor_cnt - (i*2)
    result[line-current+i] += " "*count


N = int(input())
result = ["" for _ in range(N)]


draw_stars(N, N)

floor_cnt = (N // 3)*5 + (N // 3)-1
for i in range(N):
  empty_cnt = (floor_cnt-len(result[i])) // 2
  result[i] = (" " * empty_cnt) + result[i]
  result[i] += " " * empty_cnt

print(*result, sep="\n")