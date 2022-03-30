#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int *arr;
	int i, x, y, n, m;
	
	arr = (int *)malloc(sizeof(int) * 20000005);
	i = 0;
	while (i <= 20000000)
	{
		arr[i] = 0;
		i++;
	}
	i = 0;
	scanf("%d", &n);
	while (i < n)
	{
		scanf("%d", &x);
		arr[x + 10000000]++;
		i++;
	}
	i = 0;
	scanf("%d", &m);
	while (i < m)
	{
		scanf("%d", &y);
		printf("%d ", arr[y + 10000000]);
		i++;
	}
}