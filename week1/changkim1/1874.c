#include <stdio.h>
#include <stdlib.h>

char plma[200005];
int plma_i;
int plma_tmp;
int proto = 1;

void	push(int *stack, int proto, int s_i)
{
	stack[s_i] = proto;
	plma[plma_i] = '+';
	plma_i++;
	return ;
}

void	pop(int *stack, int s_i)
{
	plma[plma_i] = '-';
	plma_i++;
	stack[s_i] = 0;
	return ;
}

int main(void)
{
	int n;
	int *stack, *result;
	
	scanf("%d", &n);
	stack = (int *)malloc(sizeof(int) * n);
	result = (int *)malloc(sizeof(int) * n);
	int i = 0;
	while (i < n)
	{
		scanf("%d", &result[i]);
		i++;
	}
	i = 0;
	int s_i = 0;
	int tmp;
	while (proto <= n + 1)
	{
		if (proto == n + 1)
		{
			printf("NO");
			return (0);
		}
		if (proto <= result[i])
		{
			push(stack, proto, s_i);
			if (proto != result[i])
				s_i++;
			proto++;
		}
		while (stack[s_i] && stack[s_i] == result[i])
		{
			pop(stack, s_i);
			s_i--;
			i++;
			if (stack[s_i] != result[i])
				s_i++;
		}
		if (!result[i])
			break ;
	}
	while (plma_tmp < plma_i)
	{
		printf("%c\n", plma[plma_tmp]);
		plma_tmp++;
	}
	return (0);
}