#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int check_pe(char *num)
{
	int f, b, len;

	f = 0;
	len = strlen(num);
	b = len - 1;
	while (num[f] == num[b] && f < b)
	{
		f++;
		b--;
	}
	if (len % 2 == 0)
	{
		if (f > b)
			return (1);
	}
	else
	{
		if (f == b)
			return (1);
	}
	return (0);
}

int main(void)
{
	char num[6];
	int check;

	while (1)
	{
		scanf("%s", num);
		if (num[0] == '0')
			break ;
		check = check_pe(num);
		check == 1 ? printf("yes\n") : printf("no\n");
	}
}