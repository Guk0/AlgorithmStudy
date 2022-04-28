#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	N, max;
	float	sum, result;
	scanf("%d", &N);

	int	*grade;
	grade = (int *)malloc(sizeof(int) * N);

	max = 0;
	sum = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &grade[i]);
		if (grade[i] > max)
			max = grade[i];
		sum += grade[i];
	}
	result = sum / (float)max / N * 100;
	printf("%f\n", result);
	return (0);
}
