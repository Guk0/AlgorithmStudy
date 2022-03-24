#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int *arr;

	arr = (int *)malloc(sizeof(int) * 10);
	int i = 0;
	while (i < 10)
	{
		arr[i] = i;
		i++;
	}
	i = 0;
	while (i < 10)
	{
		printf("%d\n", arr[i]);
		i++;
	}
	printf("%d, %d\n", (int)sizeof(arr), (int)sizeof(arr) / (int)sizeof(int));
}