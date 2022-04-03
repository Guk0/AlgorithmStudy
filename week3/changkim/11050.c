#include <stdio.h>
#include <stdlib.h>

int comb(int n, int r)
{
	if (r == 0 || r == n)
		return 1;
	return (comb(n - 1, r) + comb(n - 1, r - 1));
}

int main(void)
{
	int n, k;

	scanf("%d%d", &n, &k);
	if (k < 0 || k > n)
	{
		printf("0");
		return (0);
	}
	int result = comb(n, k);
	printf("%d", result);
}