#include <stdio.h>
#include <stdlib.h>


int	input[25][25];
int	result[500];
int n;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int compare(const void *a, const void *b)
{
	int num1 = *((int *)a);
	int num2 = *((int *)b);

	return (num1 - num2);
}

int	dfs(int x, int y, int complex)
{
	input[x][y] = complex;

	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n && input[nx][ny] == 1)
			dfs(nx, ny, complex);
	}
	return (0);
}

int main(void)
{
	int complex = 2;

	scanf("%d", &n);
	for	(int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			scanf("%1d", &input[i][j]);
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (input[i][j] == 1)
			{
				dfs(i, j, complex);
				complex++;
			}
		}
	}
	complex -= 2;
	printf("%d\n", complex);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (input[i][j] > 1)
				result[input[i][j] - 2]++;
		}
	}
	qsort(result, complex, sizeof(int), compare);
	for (int i = 0; i < complex; i++)
	{
		printf("%d\n", result[i]);
	}
}