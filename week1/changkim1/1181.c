#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct groupz {
	int len;
	char word[55];
}	groups;

int	compare2(const void *a, const void *b)
{
	if ((*(groups *)a).len == (*(groups *)b).len)
		return (strcmp((*(groups *)a).word, (*(groups *)b).word));
	else
		return (0);
}

int compare1(const void *a, const void *b)
{
	int a1 = (*(groups *)a).len;
	int b1 = (*(groups *)b).len;

	if (a1 > b1)
		return (1);
	else if (a1 < b1)
		return (-1);
	return (0);
}

int main(void)
{
	groups *group;
	int n;

	scanf("%d", &n);
	group = (groups *)malloc(sizeof(groups) * (n + 1));
	int i = 0;
	while (i < n)
	{
		scanf("%s", group[i].word);
		group[i].len = strlen(group[i].word);
		i++;
	}
	qsort(group, n, sizeof(groups), compare1);
	qsort(group, n, sizeof(groups), compare2);
	char result[n][51];
	strcpy(result[0], group[0].word);
	i = 1;
	int j = 1;
	while (i < n)
	{
		if (strcmp(result[j - 1], group[i].word))
		{
			strcpy(result[j], group[i].word);
			j++;
		}
		i++;
	}
	i = 0;
	while (i < j)
	{
		printf("%s\n", result[i]);
		i++;
	}
}