#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	K, N;
	int	*arr;
	long long	sum = 0;
	long long	tmp_max;
	long long	tmp_min = 1; // 1이 최솟값
	long long	test;
	long long	cmp = 0;

	scanf("%d %d", &K, &N);
	arr = (int *)malloc(sizeof(int) * K);

	for (int i = 0; i < K; i++)
	{
		scanf("%d", &arr[i]);
		sum += arr[i];
	}
	// 입력받은 숫자들을 모두 더해주기 위해 long long 자료형에 저장

	tmp_max = sum / (long long)N;
	// 최댓값은 sum(총합)을 N으로 나눠준 몫에서부터 시작
	
	// 런타임 에러를 피하기 위해 최솟값과 최댓값 중간에서 시작한다
	

	tmp_max++;
	// 정답이 tmp_max인 경우 아래 반복문을 통해 정답을 구할 수 없다
	// ex) 정답이 5라면 계속 중간값들만 확인하기 때문에 2, 3, 4까지만 확인하고 4가 출력될 것이다
	// 그렇기에 tmp_max 값에 1을 더한 상태로 반복문에 들어간다
	
	while (tmp_min < tmp_max)
	{
		test = (tmp_min + tmp_max) / 2;

		for (int i = 0; i < K; i++)
		{
			cmp += arr[i] / test;
		}

		if (cmp < N)
		{
			tmp_max = test;
		}
		else if (cmp >= N)
		{
			tmp_min = test;
		}
		
		if (tmp_min + 1 == tmp_max)
			break ;


		cmp = 0;
	}

	// test는 tmp_min(1) 과 tmp_max 의 중간값에서 시작,
	// test로 K개의 랜선의 길이를 나눈 값을 다 더한 값(cmp)와 N을 비교한다
	// cmp : 현재 test 길이로 만들 수 있는 랜선의 개수
	// cmp가 N보다 작으면 tmp_max를 중간값(test)으로 줄여주고
	// cmp가 N보다 크면 tmp_min을 중간값(test)으로 늘여준다
	// tmp_min과 tmp_max의 차이가 1인 경우 tmp_min의 값이 결과값이 된다

	printf("%d", (int)tmp_min);

	free(arr);
	return (0);

}
