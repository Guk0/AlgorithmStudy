#include <stdio.h>
#include <limits.h>

int lan[10001];
int n, k, count;
long long low, high, mid, ans;

int main(void)
{
	low = 0;
	high = LLONG_MAX;
	scanf("%d %d", &k, &n);
	for (int i = 0; i < k; i++)
		scanf("%d", &lan[i]);
	
	while (low <= high)
	{
		count = 0;
		mid = (low + high) / 2;
		for (int i = 0; i < k; i++)
			count += (lan[i] / mid);
		if (count >= n)
		{
			low = mid + 1;
			if (ans < mid)
				ans = mid;
		}
		else
			high = mid - 1;
	}
	printf("%lld\n", ans);
}