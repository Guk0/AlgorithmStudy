#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int n, result;
	char *str;

	scanf("%d", &n);
	str = (char *)malloc(n + 1);
	scanf("%s", str);
	int i = 0;
	result = 0;
	while (i < n)
	{
		result += str[i] - 48;
		i++;
	}
	printf("%d", result);
}