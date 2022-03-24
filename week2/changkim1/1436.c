#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char	*plus_itoa(int a)
{
	char *str;
	int ten_count, i, tmp_a;

	i = 0;
	ten_count = 0;
	tmp_a = a;
	while (tmp_a > 0)
	{
		tmp_a /= 10;
		ten_count++;
	}
	str = (char *)malloc(sizeof(char *) * (ten_count + 1));
	i = ten_count - 1;
	str[ten_count] = 0;
	while (i >= 0)
	{
		str[i] = a % 10 + '0';
		a /= 10;
		i--;
	}
	return (str);
}

int main(void)
{
	int n, i, count;
	char *str;

	scanf("%d", &n);
	i = 666;
	count = 0;
	while (count <= 10000)
	{
		if (strstr(str = plus_itoa(i), "666"))
			count++;
		if (count == n)
			break ;
		free(str);
		i++;
	}
	printf("%d", i);
}