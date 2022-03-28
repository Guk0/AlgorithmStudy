#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int stack[10000];
char com[10000][7];
int x[10000];
int count;
int n;

void	push(int x)
{
	stack[count] = x;
	count++;
}

void	pop(void)
{
	if (count == 0)
		printf("-1\n");
	else 
	{
		count--;
		printf("%d\n", stack[count]);
		stack[count] = 0;
	}
}

void	size(void)
{
	printf("%d\n", count);
}

void	empty(void)
{
	if (count == 0)
		printf("1\n");
	else
		printf("0\n");
}

void	top(void)
{
	if (count == 0)
		printf("-1\n");
	else
		printf("%d\n", stack[count - 1]);
}

int main(void)
{
	int i;
	 
	i = 0;
	scanf("%d", &n);
	while (i < n)
	{
		scanf("%s", com[i]);
		if (com[i][1] == 'u')
			scanf("%d", &x[i]);
		i++;
	}
	i = 0;
	while (i < n)
	{
		if (com[i][1] == 'u')
			push(x[i]);
		else if (com[i][0] == 'p')
			pop();
		else if (com[i][0] == 's')
			size();
		else if (com[i][0] == 'e')
			empty();
		else if (com[i][0] == 't')
			top();
		i++;
	}
}