#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int several(int i)
{
	int sev;

	sev = 0;
	while (i > 0)
	{
		sev += i % 10;
		i /= 10;
	}
	return (sev);
}

int main(void)
{
	int i, tmp, n;

	i = 0;
	scanf("%d", &n);
	while (i < n)
	{
		if (several(i) + i == n)
		{
			printf("%d", i);
			return (0);
		}
		i++;
	}
	printf("0");
	return (0);
}