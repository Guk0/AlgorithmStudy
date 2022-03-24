#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct que {
	int n;
	int m;
	char *imp;
}	ques;

int	max_idx(char *imp, int chong)
{
	int i, idx;

	i = 0;
	idx = i;
	i++;
	while (i < chong)
	{
		if (imp[idx] < imp[i])
			idx = i;
		i++;
	}
	return (idx);
}

char	*str_join(char *imp)
{
	char *result, *tmp;
	int len, max, i;

	len = strlen(imp);
	result = (char *)malloc(sizeof(char) * len);
	tmp = (char *)malloc(sizeof(char) * len);
	max = max_idx(imp, len);
	i = 0;
	while (i < max)
	{
		tmp[i] = imp[i];
		i++;
	}
	i++;
	int j = 0;
	while (i < len)
	{
		result[j] = imp[i];
		i++;
		j++;
	}
	i = 0;
	while (j < len)
	{
		result[j] = tmp[i];
		i++;
		j++;
	}
	result[j] = 0;
	free(tmp);
	free(imp);
	return (result);
}


int	make_result(char *imp, int n, int m)
{
	int count, me, chong, max;

	chong = n;
	me = m;
	count = 0;
	char *tmp;
	while (chong > 0)
	{
		max = max_idx(imp, chong);
		if (me == max)
		{
			count++;
			return (count);
		}
		else
		{
			if (me < max)
				me = chong - max + me - 1;
			else
				me = me - max - 1;
			chong--;
			count++;
		}
		imp = str_join(imp);
	}
}

int main(void)
{
	int t, i, j;
	ques *que;

	scanf("%d", &t);
	que = (ques *)malloc(sizeof(ques) * t);
	i = 0;
	while (i < t)
	{
		scanf("%d%d", &que[i].n, &que[i].m);
		que[i].imp = (char *)malloc(sizeof(char) * (que[i].n + 1));
		j = 0;
		while (j < que[i].n)
		{
			scanf(" %c", &que[i].imp[j]);
			j++;
		}
		i++;
	}
	int *result;
	result = (int *)malloc(sizeof(int) * t);
	i = 0;
	while (i < t)
	{
		result[i] = make_result(que[i].imp, que[i].n, que[i].m);
		printf("%d\n", result[i]);
		i++;
	}
	free((void *)que);
	free((void *)result);
}