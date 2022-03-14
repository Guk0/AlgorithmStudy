#include <stdio.h>
#include <string.h>

char	str[1000001];
int	check[26] = {0};

// ASCII 65 = 'A'  97 = 'a'  63 = '?'

char	most(int *check)
{
	char	a = 0;
	char	flag = 0;

	for (int i = 0; i < 26; i++)
	{
		if (a != i && check[a] == check[i])
			flag = 1;
		if (check[a] < check[i])
		{
			a = i;
			flag = 0;
		}
	}
	if (flag)
		return ('?');
	else
		return (a + 'A');
}

int	main(void)
{
	int	len;

	scanf("%s", str);
	len = strlen(str);
	for (int i = 0; i < len; i++)
	{
		if (str[i] >= 'a' && str[i] <= 'z')
			(check[str[i] - 'a'])++;
		else
			(check[str[i] - 'A'])++;
	}
	printf("%c", most(check));

	return (0);
}
