#include <stdio.h>

int	main(void)
{
	int	N;
	int	result = 0;
	char	tmp = 0;
	
	scanf("%d\n", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%c", &tmp);
		result += (tmp - '0');
	}
	printf("%d\n", result);
	return (0);
}
