#include <stdio.h>
#include <stdlib.h>

int n, m;
int	tree[1000001];

int compare(const void *a, const void *b)
{
	int a1 = *(int *)a;
	int b1 = *(int *)b;
	return (b1 - a1);
}

int check(const int mid)
{
	long long sum = 0;
	int	i;

	i = 0;
	while (i < n)
	{
		if (tree[i] > mid)
			sum += (tree[i] - mid);
		i++;
	}
	return (sum >= m);
}

int main(void)
{
	int low;
	int high;
	int mid;

	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%d", &tree[i]);
	qsort(tree, n, sizeof(int), compare);
	low = 0;
	high = tree[0];
	while (low + 1 < high)
	{
		mid = (low + high) / 2;
		if (check(mid) != 0)
			low = mid;
		else
			high = mid;
	}
	printf("%d\n", low);
}