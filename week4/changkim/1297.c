#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
	double h, w, d;
	double a, b, x, tmp;

	scanf("%lf%lf%lf", &d, &h, &w);
	x = (d * d) / (h * h + w * w);
	a = h * h * x;
	b = w * w * x;
	a = (int)(sqrt((double)a));
	b = (int)(sqrt((double)b));
	printf("%d %d", (int)a, (int)b);
}