#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX 5000000

int num[MAX];
int average;
int median;
int mode;
int range;

int compare(const void *a, const void *b)
{
	int num1 = *(int *)a;
	int num2 = *(int *)b;

	return (num1 - num2);
}

int _ave(int *num, int n)
{
	int res, i;
	int tmp1 = 0;
	double tmp2;

	i = 0;
	while (i < n)
	{
		tmp1 += num[i];
		i++;
	}
	tmp2 = (double)tmp1 / (double)n;
	res = (int)round(tmp2);
	return (res);
}

int _median(int *num, int n)
{
	qsort(num, n, sizeof(int), compare);
	return (num[n / 2]);
}


int _mode(int *num, int n)
{
	int flag;
	int most;
	int i;
	int res;
	int check[8005] = { 0 };

	i = 0;
	flag = 0;
	most = 1;
	while (i < n)
	{
		check[num[i] + 4000]++;
		i++;
	}
	i = 0;
	while (i < 8005)
	{
		most = most > check[i] ? most : check[i];
		i++;
	}
	i = 0;
	while (i < 8005)
	{
		if (most == check[i])
		{
			flag++;
			res = i - 4000;
		}
		if (flag == 2)
			return (res);
		i++;
	}
	return (res);
}

int _range(int *num, int n)
{
	return (num[n - 1] - num[0]);
}

int main(void)
{
	int n;
	int i;

	scanf("%d", &n);
	i = 0;
	while (i < n)
	{
		scanf("%d", &num[i]);
		i++;
	}
	average = _ave(num, n);
	median = _median(num, n);
	mode = _mode(num, n);
	range = _range(num, n);
	printf("%d\n%d\n%d\n%d", average, median, mode, range);
}