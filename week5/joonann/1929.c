#include <stdio.h>
#include <math.h>

// 소수는 1보다 큰 자연수 중에서 약수를 1과 자기 자신만 갖는 수

int	prime(int N)
{
	int	sqrt_N;

	sqrt_N = (int)sqrt((double)N);
	// 양수에서는 double > int 형변환이 내림하는 효과를 갖는다

	if (N == 1)
		return (0);
	if (N == 2 || N == 3)
		return (1);
	for (int i = 2; i <= sqrt_N; i++)
	{
		if (N % i == 0)
			return (0);
	}
	return (1);
}
// 소수인지 아닌지 판단하는 함수
// N을 N의 제곱근까지 나누어봤을 때
// 나누어 떨어지는 수가 하나라도 있으면 소수가 아니다
// 소수가 아니라면 0을 반환,
// 소수라면 1을 반환 

int	main(void)
{
	int	N, M;

	scanf("%d %d", &N, &M);
	while (N <= M)
	{
		if (prime(N))
			printf("%d\n", N);
		N++;
	}
	return (0);
}
