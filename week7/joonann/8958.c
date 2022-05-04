#include <stdio.h>

int	main(void)
{
	int	N, score;
	char	check, flag;

	scanf("%d\n", &N);
	for (int i = 0; i < N; i++)
	{
		score = 0;
		flag = 0;
		while (1)
		{
			scanf("%c", &check);
			if (check != 'O' && check != 'X')
				break ;
			if (check == 'O' && flag)
				flag++;
			else if (check == 'O')
				flag = 1;
			else 
			{
				flag = 0;
				continue ;
			}
			score += flag;
		}
		printf("%d\n", score);
	}

	return (0);
}
