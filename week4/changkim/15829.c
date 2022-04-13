#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int r = 31;
int m = 1234567891;

int abc[26];
char alp[27];

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
		result += (int)(str[i] - 96) * (int)pow(r, i);
		i++;
	}
	result = result % m;
	printf("%lld", result);
}