#include <stdlib.h>
#include <stdio.h>

#define min(a, b) (a < b ? a : b)

int n;
int R[100000] = { 0 };

int main(void)
{
	int i;

	R[1] = R[2] = R[5] = R[7] = 1;
	R[3] = R[4] = R[6] = 2;
	scanf("%d", &n);
	if (n < 8)
	{
		printf("%d", R[n]);
		return (0);
	}
	i = 8;
	while (i <= n)
	{
		R[i] = min(min(R[i - 1] + R[1], R[i - 2] + R[2]), min(R[i - 5] + R[5], R[i - 7] + R[7]));
		i++;
	}
	i--;
	printf("%d", R[i]);
}