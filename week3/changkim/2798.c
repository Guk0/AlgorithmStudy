#include <stdio.h>

#define MAX 100
int n, m, result;
int card[MAX];

int main(void)
{
	int i, j, k;

	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%d", &card[i]);
	for (i = 0; i < n; i++)
	{
		for (j = i + 1; j < n; j++)
		{
			for (k = j + 1; k < n; k++)
			{
				if (card[i] + card[j] + card[k] <= m)
					result = result > card[i] + card[j] + card[k] ? result : card[i] + card[j] + card[k];
			}
		}
	}
	printf("%d", result);
}