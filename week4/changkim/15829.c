#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int r = 31;
int m = 1234567891;

int abc[26];
char alp[27];

int jegop(int i, int count)
{
	int tmp;
	int result;

	result = 1;
	while (count > 0)
	{
		result = result * i;
		if (result >= m)
			result = result % m;
		count--;
	}
}

int main(void)
{
	int l, i;
	long long int result;
	char *str;

	i = 0;
	result = 0;
	scanf("%d", &l);
	str = (char *)malloc(sizeof(char) * (l + 1));
	scanf("%s", str);
	while (i < l)
	{
		result += (int)(str[i] - 96) * jegop(r, i);
		i++;
	}
	result = result % m;
	printf("%lld", result);
}