#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10000

char com[MAX + 1][11];
int back;
int push[MAX];
int deque[MAX];

void	push_front(int x)
{
	int i;

	i = back;
	if (back != 0)
	{
		while (i >= 0)
		{
			deque[i + 1] = deque[i];
			i--;
		}
	}
	deque[0] = x;
	back++;
}

void	push_back(int x)
{
	deque[back] = x;
	back++;
}

void	pop_front(void)
{
	int i;

	i = 1;
	if (back != 0)
	{
		printf("%d\n", deque[0]);
		while (i < back)
		{
			deque[i - 1] = deque[i];
			i++;
		}
		back--;
	}
	else
		printf("-1\n");
}

void	pop_back(void)
{
	if (back != 0)
	{
		back--;
		printf("%d\n", deque[back]);
		deque[back] = 0;
	}
	else
		printf("-1\n");
}

void	size(void)
{
	printf("%d\n", back);
}

void	empty()
{
	back == 0 ? printf("1\n") : printf("0\n");
}

void	front()
{
	back == 0 ? printf("-1\n") : printf("%d\n", deque[0]);
}

void	back_()
{
	back == 0 ? printf("-1\n") : printf("%d\n", deque[back - 1]);
}

int	com_check(char *com, int x)
{
	if (!strncmp(com, "push_front", 10))
		push_front(x);
	else if (!strncmp(com, "push_back", 10))
		push_back(x);
	else if (!strcmp(com, "pop_front"))
		pop_front();
	else if (!strcmp(com, "pop_back"))
		pop_back();
	else if (!strcmp(com, "size"))
		size();
	else if (!strcmp(com, "empty"))
		empty();
	else if (!strcmp(com, "front"))
		front();
	else if (!strcmp(com, "back"))
		back_();
	return (1);
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
		if (!strncmp(com[i], "push", 4))
			scanf("%d", &push[i]);
		i++;
	}
	for (i = 0; i < n; i++)
		com_check(com[i], push[i]);
}