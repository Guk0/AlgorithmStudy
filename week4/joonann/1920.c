#include <stdio.h>
#include <stdlib.h>

void	sort_arr(int *arr, int	N)
{
	int	tmp;

	for (int i = 0; i + 1 < N; i++)
	{
		for (int j = i + 1; j < N; j++)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
}
// 배열의 요소를 크기 순서대로 정렬해주는 함수
// 정렬 후 찾으려는 숫자가  정렬한 배열의 중간값 기준으로 큰지 작은지 판단한다
// 그보다 큰/작은 범위의 중간값을 새로운 기준으로 삼아 크기를 판단하고 이 과정을 반복해서
// 가장 빠른 방법으로 배열에 들어있는 숫자인지 확인한다

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
// tmp - 1 해준 이유는 n번째 인덱스 요소는 arr[n - 1]이기 때문
// first와 last가 1 차이날 때까지 반복해서 중간요소(인덱스 : (first + last) / 2)와 비교한 다음
// first나 last를 중간 인덱스로 바꿔주면서 확인하는 범위를 줄여나간다
// num이 중간값 중 하나라도 같은 숫자가 있으면  1 반환, 반복문을 빠져나온 다음 first와 last가 1차이날 때 arr[first], arr[last]와 같은 것이 있다면 1 반환
// arr[first] ~ arr[last]의 범위를 벗어났거나 위 과정에서 1을 반환하지 못한 경우 0 반환

int	main(void)
{
	int	N = 0;
	int	M = 0;
	int	*arr_n;
	int	num = 0;

	scanf("%d", &N);
	arr_n = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr_n[i]);
	sort_arr(arr_n, N);
	scanf("%d", &M);
	for (int i = 0; i < M; i++)
	{
		scanf("%d", &num);
		printf("%d\n", find_num(num, arr_n, N));
	}
	free(arr_n);
	return (0);
}
