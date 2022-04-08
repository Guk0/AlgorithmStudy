#include <stdio.h>
#include <stdlib.h>

int	compare(const void *a, const void *b)
{
	if (*(int *)a > *(int *)b)
		return (1);
	else if (*(int *)a == *(int *)b)
		return (0);
	else
		return (-1);
}

int	main(void)
{
	int	N, sum, max, min, mid, mode, sign;
	int	*list;
	int	mode1, mode2, freq, j, m, check;
	float	avg;
	
	sum = 0;

	scanf("%d", &N);
	list = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &list[i]);
		sum += list[i];
	}

	qsort(list, N, sizeof(int), compare);
	// qsort 정렬을 이용해 오름차순으로 배열을 정렬한 다음 계산한다
	
	mode1 = 0;
	freq = 0;
	j = 0;
	m = 0;
	while (j < N)
	{
		while (list[j] == list[j + m])
			m++;
		j += m;
		if (freq < m)
		{
			freq = m;
			mode1 = j - 1;
			mode2 = j - 1;
			check = 1;
		}
		else if (freq == m && check == 1)
		{
			mode2 = j - 1;
			check = 0;
		}
		m = 0;
	}
	// 최빈값의 인덱스를 구하는 반복문, 최빈값이 두 개 이상인 경우 두 번째로 작은 최빈값의 인덱스가 mode2에 할당된다

	sign = 1;
	avg = (float)sum / N;
	if (avg < 0)
	{
		sign *= -1;
		avg *= -1;
	}
	if (avg - (int)avg >= 0.5)
	{
		if (avg >= 0)
			avg = avg + 1;
		else
			avg = avg - 1;
	}
	avg = avg * sign;
	// avg의 절대값을 반올림해줘야 한다. 소수점 아래가 0.5보다 큰지 작은지에 따라서 절대값에 1을 더해준다

	max = list[N - 1];
	min = list[0];
	mid = list[N / 2];
	mode = list[mode2];
	// max 는 제일 끝 인덱스 min은 첫 인덱스, mid는 중간 인덱스를 택하면 된다
	// (인덱스의 개수가 항상 홀수이기 때문에 2로 나눈 몫이 중간값이 됨)
	// 최빈값이 한 개이든 여러 개이든 mode2의 인덱스값이 항상 문제에서 요구하는 최빈값이 된다(조건문 한 번 더 쓰기 싫었음)



	printf("%d\n%d\n%d\n%d\n", (int)avg, mid, mode, max - min);

	free(list);
	return (0);
}
