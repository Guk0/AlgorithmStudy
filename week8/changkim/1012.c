#include <stdio.h>
#include <memory.h>
#define M  51

int w, h, t, k, count;
int visit[M][M];
int input[M][M];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int head, tail;

typedef struct node {
	int x;
	int y;
}node;

node que[2500];

node	Deque(void)
{
	node tmp;
	tmp = que[head];
	head = (head + 1) % 2500;
	return (tmp);
}

void	Enque(int x, int y)
{
	node tmp;
	tmp.x = x;
	tmp.y = y;
	que[tail] = tmp;
	tail = (tail + 1) % 2500;
}

int is_empty(void)
{
	if (head == tail)
		return (0);
	else
		return (1);
}

void	BFS(int i, int j)
{
	int nx, ny;

	Enque(i, j);
	visit[i][j] = 1;
	while (is_empty())
	{
		node tmp;
		tmp = Deque();
		for (int i = 0; i < 4; i++)
		{
			nx = tmp.x + dx[i];
			ny = tmp.y + dy[i];
			if (nx >= 0 && nx < h && ny >= 0 && ny < w)
			{
				if (!visit[nx][ny] && input[nx][ny])
				{
					Enque(nx, ny);
					visit[nx][ny] = 1;
				}
			}
		}
	}
}

int main(void)
{
	int c;
	scanf("%d", &t);

	c = 0;
	while (c < t)
	{
		scanf("%d %d %d", &w, &h, &k);
		count = 0;
		memset(visit, 0, sizeof(visit));
		memset(input, 0, sizeof(input));
		int z = 0;
		int x, y;
		while (z < k)
		{
			scanf("%d %d", &x, &y);
			input[y][x] = 1;
			z++;
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (!visit[i][j] && input[i][j])
				{
					BFS(i, j);
					count++;
				}
			}
		}
		printf("%d\n", count);
		c++;
	}
}