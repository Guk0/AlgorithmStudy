#include <stdlib.h>
#include <stdio.h>

// int	make_arr(int *arr, int idx, int n)
// {
// 	if (idx == n || idx == -3)
// 	{
// 		return (-3);
// 	}
// 	else if (arr[idx] > 0)
// 	{
// 		idx++;
// 	}
// 	else if (arr[idx] == 0)
// 	{
// 		arr[idx] = -1;
// 		idx--;
// 		while (arr[idx] == -1)
// 			idx--;
// 		arr[idx] = -1;
// 	}
// 	else if (arr[idx] == -1)
// 	{
// 		idx++;
// 	}
// 	idx = make_arr(arr, idx, n);
// 	return (idx);
// }

int count;
int stack[100000];

void push_pop(int x)
{
	if (x == 0)
	{
		count--;
		stack[count] = 0;
	}
	else
	{
		stack[count] = x;
		count++;
	}
}

int main(void)
{
	int n, x;

	scanf("%d", &n);
	int i = 0;
	while (i < n)
	{
		scanf("%d", &x);
		push_pop(x);
		i++;
	}
	i = 0;
	int result = 0;
	while (i < n)
	{
		result += stack[i];
		i++;
	}
	printf("%d", result);
}