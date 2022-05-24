#include <stdio.h>
#include <string.h>
#define MAX 1000001

int stack[MAX];
int input[MAX];
int number[MAX];
char	result[MAX];

int idx, res;
int n;

void	push(int x)
{
	stack[idx] = x;
	result[res] = '+';
	res++;
	idx++;	
}

int	pop(void)
{
	int x;

	idx--;
	x = stack[idx];
	stack[idx] = 0;
	result[res] = '-';
	res++;
}

int main(void)
{
	int i, j, tmp;

	i = 0;
	scanf("%d", &n);
	while (i < n)
	{
		number[i] = i + 1;
		scanf("%d", &input[i]);
		i++;
	}
	i = 0;
	j = 1;
	push(number[0]);
	while (idx != 0 || input[i])
	{
		if (stack[idx - 1] == input[i])
		{
			tmp = pop();
			i++;
			continue ;
		}
		if (j >= n)
			break ;
		push(number[j]);
		j++;
		
	}
	if (i < n)
		printf("NO\n");
	else
	{
		for (int k = 0; k < strlen(result); k++)
			printf("%c\n", result[k]);
	}
}