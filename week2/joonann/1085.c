#include <stdio.h>

int	minimum(int a, int b)
{
	if (a < b)
		return a;
	else
		return b;
}

int	main(void)
{
	int	x, y, w, h;
	int	result1;
	int	result2;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	result1 = minimum(x, w - x);
	result2 = minimum(y, h - y);
	printf("%d", minimum(result1, result2));
	return (0);
}
