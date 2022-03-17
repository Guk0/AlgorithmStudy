#include <stdlib.h>
#include <stdio.h>

typedef struct building {
	int h;
	int w;
	int n;
}	build;

typedef struct result {
	int x;
	int y;
}	result;

int main(void)
{
	build *num;
	result *results;
	int t, i, x, y;

	scanf("%d", &t);
	num = (build *)malloc(sizeof(build) * (t));
	results = (result *)malloc(sizeof(result) * (t));
	i = 0;
	while (i < t)
	{
		scanf("%d%d%d", &num[i].h, &num[i].w, &num[i].n);
		results[i].y = num[i].n % num[i].h;
		results[i].x = num[i].n / num[i].h + 1;
		i++;
	}
	i = 0;
	while (i < t)
	{
		if (results[i].y == 0)
		{
			results[i].y = num[i].h;
			results[i].x--;
		}
		printf("%d", results[i].y);
		if (results[i].x < 10)
			printf("0");
		printf("%d\n", results[i].x);
		i++;
	}
}