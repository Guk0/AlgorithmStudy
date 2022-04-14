#include <stdio.h>
#include <stdlib.h>

#define MAX 3000000

int x;
char s[6];
int set[21];

void	add(int x)
{
	set[x] = 1;
	return ;
}

void	rem(int x)
{
	set[x] = 0;
	return ;
}

void	check(int x)
{
	if (set[x] == 1)
		printf("1\n");
	else
		printf("0\n");
	return ;
}

void	toggle(int x)
{
	if (set[x] == 1)
		set[x] = 0;
	else
		set[x] = 1;
	return ;
}

void	all(void)
{
	int i;

	i = 0;
	while (i <= 21)
	{
		set[i] = 1;
		i++;
	}
	return ;
}

void	empty(void)
{
	int i;

	i = 0;
	while (i <= 21)
	{
		set[i] = 0;
		i++;
	}
	return ;
}


int main(void)
{
	int m;
	int i;

	scanf("%d", &m);
	i = 0;
	while (i < m)
	{
		scanf("%s", s);
		if (s[1] != 'l')
		{
			scanf("%d", &x);
			if (s[0] == 'a')
				add(x);
			else if (s[0] == 'r')
				rem(x);
			else if (s[0] == 'c')
				check(x);
			else if (s[0] == 't')
				toggle(x);
			else if (s[0] == 'e')
				empty();
		}
		else
			all();
		i++;
	}
}