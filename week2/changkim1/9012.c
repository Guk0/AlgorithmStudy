#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 51


typedef struct check {
	int count;
	int idx;
} check;

check VPS_check(char *str, check check)
{
	if (check.count < 0)
		return (check);
	else if (str[check.idx] == ')' || str[check.idx] == '(')
	{
		if (str[check.idx] == ')')
		{
			check.count--;
			check.idx++;
		}
		else if (str[check.idx] == '(')
		{
			check.idx++;
			check.count++;
		}
		check = VPS_check(str, check);
	}
	return (check);
}

int main(void)
{
	int i, t;
	char **str;

	i = 0;
	scanf("%d", &t);
	str = (char **)malloc(sizeof(char *) * (t + 1));
	while (i < t)
	{
		str[i] = (char *)malloc((MAX));
		scanf("%s", str[i]);
		i++;
	}
	i = 0;
	check check;
	while (i < t)
	{
		check.idx = 0;
		check.count = 0;
		check = VPS_check(str[i], check);
		if (check.count != 0)
			printf("NO\n");
		else
			printf("YES\n");
		i++;
	}
}