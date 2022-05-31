#include <stdio.h>
#include <memory.h>
#define MAX 1001

typedef struct node {
	int x;
	int y;
}	node;

node que[MAX * MAX];

int head, tail;
int sep;

int vis[MAX][MAX];
int map[MAX][MAX];

int m, n, day;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

node	Deque(void)
{
	node tmp;
	tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return (tmp);
}

void	Enque(int x, int y)
{
	que[tail].x = x;
	que[tail].y = y;
	tail = (tail + 1) % (MAX * MAX);
}

int isFull(void)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 0)
				return (0);
		}
	}
	return (1);
}

int isValid(int nx, int ny)
{
	if (nx >= 0 && nx < n && ny >= 0 && ny < m)
		return (1);
	return (0);
}

int main(void)
{
	memset(que, -1, sizeof(que));
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			scanf(" %d", &map[i][j]);
			if (map[i][j] == 1)
			{
				Enque(i, j);
				vis[i][j] = 1;
			}
		}
	}
	if (isFull() == 1)
	{
		printf("0\n");
		return (0);
	}
	sep = tail;
	while (head != tail)
	{
		int nx;
		int ny;
		node cur = Deque();
		for (int i = 0; i < 4; i++)
		{
			nx = cur.x + dx[i];
			ny = cur.y + dy[i];
			if (isValid(nx, ny) && map[nx][ny] == 0 && vis[nx][ny] != 1)
			{
				Enque(nx, ny);
				vis[nx][ny] = 1;
				map[nx][ny] = 1;
			}
		}
		if (sep == head)
		{
			day++;
			sep = tail;
			// printf("\n%d일", day);
			// for(int i = 0; i < n; i++)
			// {
			// 	printf("\n");
			// 	for (int j = 0; j < m; j++)
			// 		printf("%d ", map[i][j]);
			// }
			// printf("\n");
			if (isFull() == 1)
			{
				printf("%d\n", day);
				return (0);
			}
		}
	}
	printf("-1\n");
	return 0;
}
