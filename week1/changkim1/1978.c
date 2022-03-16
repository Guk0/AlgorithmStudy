#include <stdlib.h>
#include <stdio.h>

int n;
int arr[100];

int	is_it_sosu(int arr)
{
	int i = 2, j = 1;

	if (arr == 1)
		return (0);
	while (i * i <= arr)
	{
		if (i * i == arr)
			return (0);
		if (arr % i == 0)
			return (0);
		i++;
	}
	return (1);
}

int main(void)
{
	int result, i;

	result = 0;
	scanf("%d", &n);
	while (i < n)
	{
		scanf("%d", &arr[i]);
		i++;
	}
	i = 0;
	while (i < n)
	{
		result += is_it_sosu(arr[i]);
		i++;
	}
	printf("%d", result);
}