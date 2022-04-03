#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
	int n;
	int t;

	n = 7;
	t = 2;
	double result = (double)n / (double)t;
	printf("%d\n%d\n", n, t);
	printf("%f", result);
}