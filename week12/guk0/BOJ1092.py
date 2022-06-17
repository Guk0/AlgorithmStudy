# https://www.acmicpc.net/problem/1092
# 배

from sys import stdin
input = stdin.readline

def load_cargos():
  time = 0
  max_crains = max(crains)

  while cargos and cargos[0] <= max_crains:
    for i in range(N):
      j = 0

      while cargos and len(cargos) > j:
        if crains[i] >= cargos[j]:
          cargos.pop(j)
          break

        j += 1

    time += 1

  return -1 if cargos else time

N = int(input())
crains = list(map(int, input().split()))
M = int(input())
cargos = list(map(int, input().split()))

crains.sort(reverse=True)
cargos.sort(reverse=True)


print(load_cargos())

