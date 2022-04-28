#include <stdio.h>

int	main(void)
{
	int	N, K, result;

	scanf("%d %d", &N, &K);
	if (N - K < K)
		K = N - K; // 반복을 줄일 수 있도록 K의 값을 바꾼다
	result = 1;
	for (int i = 0; i < K; i++)
	{
		result *= N;
		N--;
	}
	while (K > 0)
	{
		result /= K;
		K--;
	}
	printf("%d", result);
	return (0);
}
// C(N, K) 이항계수를 구해서 출력한다
