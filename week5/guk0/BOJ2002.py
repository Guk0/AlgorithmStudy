from sys import stdin

input = stdin.readline

N = int(input())

in_dict = {input().strip(): i for i in range(N)}
out_list = [input().strip() for _ in range(N)]

cnt = 0

for i in range(N-1):
  for j in range(i+1, N):
    if in_dict[out_list[i]] > in_dict[out_list[j]]:
      cnt += 1
      break

print(cnt)



# 1
# 2
# 3
# 4
# 5


# 5
# 4
# 3
# 2
# 1
