# include <stdio.h>
# include <stdlib.h>
# define SWAP(x, y, tmp) ((tmp) = (x), (x) = (y), (y) = (tmp))

int	partition(int *list, int left, int right)
{
	int	low, high, tmp;
	int	pivot;

	pivot = list[left];
	low = left + 1;
	high = right;

	while (low < high)
	{
		while (low < high && list[low] < pivot)
			low++;
		while (low < high && list[high] > pivot)
			high--;
		if (low < high)
			SWAP(list[low], list[high], tmp);
	}
	if (high == right && list[left] > list[right])
		high++;
	SWAP(list[left], list[high - 1], tmp);

	return (high - 1);
}
//퀵정렬 구현

void	quick_sort(int *list, int left, int right)
{
	int	p;

	if (left < right)
	{
		p  = partition(list, left, right);

		quick_sort(list, left, p - 1);
		quick_sort(list, p + 1, right);
	}
	return ;
}

int	find_num(int num, int *arr, int arr_size)
{
	int	first = 0;
	int	last = arr_size - 1;
	int	tmp;

	if (num < arr[first] || num > arr[last])
		return (0);
	while (first != last)
	{
		if (num == arr[first] || num == arr[last])
			return (1);
		tmp = (first + last) / 2;
		if (num > arr[tmp])
			first = tmp + 1;
		else if (num < arr[tmp])
			last = tmp - 1;
		else
			return (1);
	}
	return (0);
}

int	main(void)
{
	int	N, M, num;
	int	*list;
	int	left, right;


	scanf("%d", &N);
	list = (int *)malloc(sizeof(int) * N);

	left = 0;
	right = N - 1;

	for (int i = 0; i < N; i++)
		scanf("%d", &list[i]);

	quick_sort(list, left, right);
	
	scanf("%d", &M);
	
	for (int j = 0; j < M; j++)
	{
		scanf("%d", &num);
		printf("%d\n", find_num(num, list, N));
	}

	free(list);
	return (0);
}
