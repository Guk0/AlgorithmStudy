#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int			N, K;
	int			*arr;
	unsigned long long	sum = 0;
	unsigned long long	tmp_max;
	int			tmp_N;

	scanf("%d %d", &K, &N);
	arr = (int *)malloc(sizeof(int) * K);
	for (int i = 0; i < K; i++)
	{
		scanf("%d", &arr[i]);
		sum += arr[i]; // 입력받은 숫자들을 모두 더해주기 위해 unsigned long long 자료형에 저장
	}
	tmp_max = sum / N;
	// 최댓값은 sum을 N으로 나눈 값,  1씩 최댓값을 낮춰서 가능한 결과값인지 확인해본다

	int	j;

	while (tmp_max > 1)
	{
		j = 0;
		tmp_N = N;
		while (j < K)
		{
			tmp_N -= (arr[j] / (int)tmp_max);
			if (tmp_N <= 0)
				break ;
			j++;
		}
		if (tmp_N <= 0)
			break ;
		tmp_max--;
	}
	printf("%d", (int)tmp_max);

	// K에서 한 랜선으로 만드는 tmp_max길이의 랜선의 개수 (arr[i] / tmp_max)를 반복해서 빼주는데
	// K가 0 이하가 되면 K개의 tmp_max 길이 랜선을 만들 수 있다고 판단할 수 있다
	// 이 경우, 반복문을 모두 깬 다음 tmp_max를 그대로 출력한다
	// 만약 tmp_max가 1까지 작아졌다면 while반복문에 들어가지 않고 바로 1을 출력하도록 구현했다

	free(arr);
}
