#include <stdio.h>
#include <stdlib.h>

int	compare(const void *a, const void *b)
{
	if (*(int *)a > *(int *)b)
		return (1);
	else if (*(int *)a < *(int *)b)
		return (-1);
	else
		return (0);
}

int	find_num(int num, int *list, int size)
{
	int first = 0;
	int last = size - 1;
	int tmp;

	if (num < list[first] || num > list[last])
		return (0);
	while (first < last)
	{
		tmp = (first + last) / 2;
		if (num == list[first] || num == list[last] || num == list[tmp])
			return (1);
		if (num > list[tmp])
			first = tmp + 1;
		else if (num < list[tmp])
			last = tmp - 1;
	}
	return (0);
}

int	main(void)
{
	int N, M, num;
	int *list, *list_M;

	scanf("%d", &N);
	list = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &list[i]);
	}

	qsort(list, N, sizeof(int), compare);
	
	scanf("%d", &M);
	list_M = (int *)malloc(sizeof(int) * M);
	for (int j = 0; j < M; j++)
	{
		scanf("%d", &list_M[j]);
		list_M[j] = find_num(list_M[j], list, N);
	}
	for (int i = 0; i < M; i++)
		printf("%d\n", list_M[i]);

	free(list);
	free(list_M);

	return (0);
}
