# https://www.acmicpc.net/problem/1043
# 거짓말

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt += 1

print(cnt)




# 연쇄적으로 들어가는 상황을 고려하지 않음.
# 증인 : {1}
# 파티(가) : {5, 6}
# 파티(나) : {4, 5}
# 파티(다) : {3, 4}
# 파티(라) : {2, 3}
# 파티(마) : {1, 2}



# from sys import stdin

# input = stdin.readline

# N, M = map(int, input().split())
# visited = [False] * M

# truth = list(map(int, input().split()))
# truth_arr = truth[1:] if truth[0] > 0 else []

# arr = []
# graph = {i: True for i in range(1, N+1)}

# answer = 0

# for i in range(M):
#   party = list(map(int, input().split()))
#   sliced = party[1:]
#   arr.append(sliced)

#   tmp_normal = []
#   tmp_truth = []
#   for el in sliced:
#     if el in truth_arr:
#       tmp_truth.append(el)
#     else:
#       tmp_normal.append(el)

#   for el1 in tmp_truth:  
#     # 파티 중 여기 tmp_truth 루프가 돌았다면 진실을 아는 사람이 있다는 것이기에 다시 방문할 필요 없음(1명인 경우 포함)
#     visited[i] = True
#     for el2 in tmp_normal:
#       # 해당 사람에게 거짓말 못함
#       graph[el2] = False


# for i in range(M):
#   # 2명 이상인 파티 중 visitied가 False라면 그 파티에는 진실을 아는 사람이 없는 것.  
#   if not visited[i]:
#     flag = True
#     for j in range(len(arr[i])):
#       if not graph[arr[i][j]]:
#         flag = False
#     if flag:
#       answer += 1

# print(answer)
  
    
