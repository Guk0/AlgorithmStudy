# https://www.acmicpc.net/problem/1644
# 소수의 연속합
# 에라토스테네스의 체, 투포인터

N = int(input())

arr = [i for i in range(N+1)]
is_prime = [True for _ in range(N+1)]
is_prime[0], is_prime[1] = False, False
primes = []

for i in range(2, N+1):
  if is_prime[i]:
    j = 2
    while i * j <= N:
      is_prime[i*j] = False
      j += 1

    primes.append(i) 

answer = 0
prime_sum = 0
p2 = 0

for p1 in range(len(primes)):
  prime_sum += primes[p1]
  while prime_sum > N:
    prime_sum -= primes[p2]
    p2 += 1
  
  if prime_sum == N:
    answer += 1

print(answer)