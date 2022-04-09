#include <stdio.h>
#include <stdlib.h>
#define min(a, b) a < b ? a : b

int main(void)
{
	int x, y, w, h;
	int result;

	scanf("%d%d%d%d", &x, &y, &w, &h);
	result = min(x, y);
	result = min(result, w - x);
	result = min(result, h - y);
	printf("%d", result);
}