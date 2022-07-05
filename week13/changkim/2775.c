#include <stdio.h>
#include <memory.h>
#define MAX 15

int t, k, n;
int apart[MAX][MAX];

int main(void)
{
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++)
	{
		memset(apart, 0, sizeof(apart));
		scanf("%d %d", &k, &n);
		for (int a = 0; a <= k; a++)
		{
			for (int b = 1; b <= n; b++)
			{
				if (a == 0)
					apart[a][b] = b;
				else
				{
					apart[a][b] += apart[a - 1][b] + apart[a][b - 1];
				}
			}
		}
		printf("%d\n", apart[k][n]);
	}
}