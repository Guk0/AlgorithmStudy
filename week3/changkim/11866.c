#include <stdlib.h>
#include <stdio.h>

#define MAX 1000

int proto[MAX];
int result[MAX];
int count;

int main(void)
{
	int n, k, i, j;

	scanf("%d%d", &n, &k);
	i = 0;
	while (i < n)
	{
		proto[i] = i + 1;
		i++;
	}
	i = 0;
	j = 0;
	while (j < n)
	{
		if (proto[i] != 0)
			count++;
		if (count == k)
		{
			result[j] = proto[i];
			proto[i] = 0;
			j++;
			count = 0;
		}
		i++;
		if (i == n)
			i = 0;
	}
	i = 0;
	printf("<");
	while (i < n)
	{
		printf("%d", result[i]);
		i++;
		if (i != n)
			printf(", ");
	}
	printf(">\n");
}