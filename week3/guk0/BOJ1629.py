# https://www.acmicpc.net/problem/1629
# 곱셈
# 분할정복

# https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 지수법칙과 나머지 분배법칙 응용이 필요

A, B, C = map(int, input().split())

def divide(a, b):
  if b == 1:
    return a % C

  tmp = divide(a, b//2)
  if b % 2 == 0:
    return (tmp * tmp) % C
  else:
    return (tmp * tmp * a) % C



print(divide(A, B))

