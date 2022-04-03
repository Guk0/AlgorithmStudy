#include <stdio.h>

#define max(a, b) (a > b ? a : b)
#define min(a, b) (a > b ? a : b)

void	make_res(int one, int two, int thr)
{
	if (one * one + two * two == thr * thr)
		printf("right\n");
	else
		printf("wrong\n");
}

int main(void)
{
	int a, b, c;
	int one, two, thr;

	while (1)
	{
		scanf("%d%d%d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0)
			return (0);
		thr = max(a, (max(b, c)));
		if (a == thr)
			make_res(b, c, a);
		else if (b == thr)
			make_res(a, c, b);
		else if (c == thr)
			make_res(a, b, c);
	}
}