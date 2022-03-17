#include <stdlib.h>
#include <stdio.h>

int t;
typedef struct building{
	int h;
	int w;
	int n;
}	build;

int main(void)
{
	build *t_case;
	int i = 0;

	scanf("%d", t);
	t_case = (build *)malloc(sizeof(build) * t);
	while (i < t)
	{
		scanf("%d%d%d", t_case[i].h, t_case[i].w, t_case[i].n);
		i++;
	}
	i = 0;
	int idx = 0, x = 0, y = 0;
	while (idx < t)
	{
		x = (t_case[idx].n / t_case[idx].h) + 1;
		y = (t_case[idx].n % t_case[idx].h) + 1;
		idx++;
	}
	printf("%d%d", y, x);
}