#include <stdlib.h>
#include <stdio.h>

int	compare(const void *a, const void *b)
{
	int num1 = *(int *)a;
	int num2 = *(int *)b;

	return (num1 - num2);
}

int main(void)
{
	int n;
	int arr[1000000];
	int i;

	i = 0;
	scanf("%d", &n);
	while (i < n)
	{
		scanf("%d", &arr[i]);
		i++;
	}
	qsort(arr, n, sizeof(int), compare);
	i = 0;
	while (i < n)
	{
		printf("%d\n", arr[i]);
		i++;
	}
}