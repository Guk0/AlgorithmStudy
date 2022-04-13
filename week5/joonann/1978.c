#include <stdio.h>
#include <math.h>

int	prime_num(int n)
{
	int	sqrt_n = pow((double)n, 0.5);

	if (n == 1)
		return (0);
	if (n < 4)
		return (1);
	for (int i = 2; i <= sqrt_n; i++)
	{
		if (n % i == 0)
			return (0);
	}
	return (1);
}

int	main(void)
{
	int N, tmp, count;

	scanf("%d", &N);
	count = 0;

	for (int i = 0; i < N; i++)
	{
		scanf ("%d", &tmp);
		if (prime_num(tmp))
		{
			count++;
		}
	}
	printf("%d", count);

	return (0);
}
