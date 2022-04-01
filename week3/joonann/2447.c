#include <stdio.h>

int	recursive(int n, int i, int j)
{
	if (((i > n / 3) && (i <= n / 3 * 2)) && ((j > n / 3) && (j <= n / 3 * 2)))
		return (0);
	n /= 3;
	if (n == 1)
		return (1);
	else if (recursive(n, i % n, j % n) == 0)
		return (0);
	return (1);
}

int	main(void)
{
	int	n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (recursive(n, i + 1, j + 1) == 0)
				printf(" ");
			else
				printf("*");
			if (j + 1 == n)
				printf("\n");
		}
	}
	return (0);
}
