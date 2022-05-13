# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
# 백트래킹


from sys import stdin

input = stdin.readline


def dfs(index, sumation, operations):
  if index == N:
    answer.append(sumation)
    return

  if sum(operations) == 0:
    return


  for i in range(4):    
    if operations[i] > 0:      
      if i == 0:
        tmp_sum = sumation + arr[index]
      elif i == 1:
        tmp_sum = sumation - arr[index]
      elif i == 2:
        tmp_sum = sumation * arr[index]
      else:
        if sumation > -1:
          tmp_sum = sumation // arr[index]
        else:
          tmp_sum = (sumation * -1 // arr[index]) * -1
      
      tmp_ops = operations[:]
      tmp_ops[i] -= 1      
      dfs(index+1, tmp_sum, tmp_ops)

      



N = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
answer = []

dfs(1, arr[0], ops)

print(max(answer))
print(min(answer))