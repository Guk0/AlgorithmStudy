#include <stdio.h>

int v;
int a, b;
int tmp;

int main(void)
{
	int dis_per_day;

	scanf("%d %d %d", &a, &b, &v);
	dis_per_day = a - b;
	v = v - a;
	if (v % dis_per_day != 0)
		tmp = v / dis_per_day + 1;
	else
		tmp = v / dis_per_day;
	tmp++;
	printf("%d\n", tmp);
}