#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX 10000

char com[MAX + 1][6];
int que[MAX];
int x[MAX];
int count;

void	make_que(void)
{
	int i, j;
	int len;

	i = 0;
	len = 0;
	while (que[len] != 0)
		len++;
	len--;
	while (i < len)
	{
		que[i] = que[i + 1];
		i++;
	}
	que[i] = 0;
}

void	push(int x)
{
	que[count] = x;
	count++;
}

void	pop(void)
{
	if (count == 0)
	{
		printf("-1\n");
		return ;
	}
	count--;
	printf("%d\n", que[0]);
	make_que();
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

void	front(void)
{
	if (count == 0)
		printf("-1\n");
	else
		printf("%d\n", que[0]);
}

void	back(void)
{
	int i;

	i = 0;
	while (que[i] != 0)
	{
		i++;
	}
	i--;
	if (que[i] == 0)
		printf("-1\n");
	else
		printf("%d\n", que[i]);
}

int main(void)
{
	int n;
	int i;

	scanf("%d", &n);
	i = 0;
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
		else if (com[i][0] == 'f')
			front();
		else if (com[i][0] == 'b')
			back();
		i++;
	}
}