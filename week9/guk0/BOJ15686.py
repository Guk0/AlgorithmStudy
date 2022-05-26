# https://www.acmicpc.net/problem/15686
# 치킨 배달

def get_distance(a, b):
  return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_chicken_distance():
  min_chicken = 10e9
  for combi in combis:
    chicken_distance = 0
    for house in houses:
      min_distance = 101
      for chicken in combi:
        min_distance = min(get_distance(house, chicken), min_distance)
      chicken_distance += min_distance
    min_chicken = min(min_chicken, chicken_distance)

  return min_chicken

from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
graph = []
chickens = []
houses = []

for i in range(N):
  row = list(map(int, input().split()))
  graph.append(row)
  for j in range(N):
    if row[j] == 1:
      houses.append([i, j])
    if row[j] == 2:
      chickens.append([i, j])

combis = list(combinations(chickens, M))


print(get_chicken_distance())
