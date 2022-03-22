#include <stdlib.h>
#include <stdio.h>

typedef struct xy {
	int x;
	int y;
}	xys;

int	compare(const void *a, const void *b)
{
	int a1, a2;
	int b1, b2;

	a1 = ((xys *)a)->x;
	a2 = ((xys *)b)->x;
	b1 = ((xys *)a)->y;
	b2 = ((xys *)b)->y;

	if (b1 != b2)
		return (b1 - b2);
	else
	{
		if (a1 != a2)
			return (a1 - a2);
		else
			return (0);
	}
}

int main(void)
{
	xys *xy;
	int n;
	int i;

	scanf("%d", &n);
	xy = (xys *)malloc(sizeof(xys) * (n));
	i = 0;
	while (i < n)
	{
		scanf("%d%d", &xy[i].x, &xy[i].y);
		i++;
	}
	qsort(xy, n, sizeof(xys), compare);
	i = 0;
	while (i < n)
	{
		printf("%d %d\n", xy[i].x, xy[i].y);
		i++;
	}
	return (0);
}