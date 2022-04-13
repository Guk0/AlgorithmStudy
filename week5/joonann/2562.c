#include <stdio.h>

int	main(void)
{
	int	max = 0;
	int	n;
	int	index;

	for (int i = 1; i < 10; i++)
	{
		scanf("%d", &n);
		if (max < n)
		{
			max = n;
			index = i;
		}
	}
	printf("%d\n%d", max, index);
	return (0);

}
