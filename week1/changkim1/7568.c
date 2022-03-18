#include <stdio.h>
#include <stdlib.h>

typedef struct dungchi {
	int w;
	int h;
	int num;
}	dungchi;

int n;
int *arr;

int	how_many_big(dungchi *dung, int idx)
{
	int i;
	int count;
	
	count = 1;
	i = 0;
	while (i < n)
	{
		if (i == idx)
		{
			i++;
			continue ;
		}
		if (dung[idx].h < dung[i].h && dung[idx].w < dung[i].w)
			count++;
		i++;
	}
	return (count);
}

int main(void)
{
	dungchi *dung;
	int i = 0;

	scanf("%d", &n);
	dung = (dungchi *)malloc(sizeof(dungchi) * (n));
	arr = (int *)malloc(sizeof(int) * (n));
	while (i < n)
	{
		scanf("%d%d", &dung[i].w, &dung[i].h);
		i++;
	}
	i = 0;
	while (i < n)
	{
		dung[i].num = how_many_big(dung, i);
		i++;
	}
	i = 0;
	while (i < n)
	{
		printf("%d ", dung[i].num);
		i++;
	}
	
}