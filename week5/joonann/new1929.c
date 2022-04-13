#include <stdio.h>
#include <string.h>

// 에라토스테네스의 체를 이용한 소수 구하는 과정

int	main(void)
{
	int	N, M, i, k;
	
	scanf("%d %d", &N, &M);
	int arr[M];
	memset(arr, 0, M * sizeof(int));

	i = 0;
	arr[0] = 1;
	while (i < M)
	{
		if (arr[i] == 1)
		{
			i++;
			continue ;
		}
		arr[i] = i + 1;
		for (int j = 2; (k = j * arr[i]) <= M; j++)
		{
			arr[k - 1] = 1; 
		}
		if (arr[i] >= N)
			printf("%d\n", arr[i]);
		i++;
	}
	return (0);
}
