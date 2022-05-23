#include <stdio.h>
#include <memory.h>

typedef struct node {
	int x;
	int y;
}	node;

int head, tail;
node que[10000];
int count[101][101];
int map[101][101];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int n, m;

void	Enque(int x, int y)
{
	node tmp;
	tmp.x = x;
	tmp.y = y;
	que[tail] = tmp;
	tail = (tail + 1) % 10000;
}

node	Deque(void)
{
	node tmp;
	tmp = que[head];
	head = (head + 1) % 10000;
	return (tmp);
}

int	is_empty(void)
{
	if (head == tail)
		return (0);
	else
		return (1);
}

void	BFS(int x, int y)
{
	int i;
	int nx, ny;
	node tmp;

	i = 0;
	Enque(x, y);
	count[x][y] = 1;
	while (is_empty())
	{
		tmp = Deque();
		i = 0;
		while (i < 4)
		{
			nx = tmp.x + dx[i];
			ny = tmp.y + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m && !count[nx][ny] && map[nx][ny])
			{
				Enque(nx, ny);
				count[nx][ny] = count[tmp.x][tmp.y] + 1;
			}
			i++;
		}
	}
}

int main(void)
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%1d", &map[i][j]);
	}
	BFS(0, 0);
	printf("%d\n", count[n-1][m-1]);
}