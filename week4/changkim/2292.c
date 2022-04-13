#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i, n;

	i = 0;
	scanf("%d", &n);
	if (n == 1)
	{
		printf("%d", 1);
		return (0);
	}
	n--;
	while (n > 0)
	{
		n = n - 6 * i;
		i++;
	}
	printf("%d", i);
}