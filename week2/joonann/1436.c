#include <stdio.h>
#include <string.h>

int	ft_check(int N)
{
	int	tmp = N;

	while (tmp >= 666)
	{
		if (tmp % 1000 == 666)
			return (1);
		else
			tmp = tmp / 10;
	}
	return (-1);
}

int	main(void)
{
	int	N;
	int	result = 666;
	int	count = 0;

	scanf("%d", &N);
	while (count < N)
	{
		if (ft_check(result) == 1)
		{
			count++;
		}
		result++;
	}
	result--;
	printf("%d", result);
	return (0);

}
