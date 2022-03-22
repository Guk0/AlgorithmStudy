#include <stdio.h>
#include <stdlib.h>

#define MAX 10001

int list[MAX] = { 0 };

int main(void)
{
	int i;
	int n;

	scanf("%d", &n);
	i = 0;
	int tmp;
	while (i < n)
	{
		scanf("%d", &tmp);
		list[tmp]++;
		i++;
	}
	i = 1;
	int j = 0;
	while (i <= 10000)
	{
		if (list[i] == 0)
		{
			i++;
			continue ;
		}
		j = 0;
		while (j < list[i])
		{
			printf("%d\n", i);
			j++;
		}
		i++;
	}
}