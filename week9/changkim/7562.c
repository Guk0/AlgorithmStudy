#include <stdio.h>
#include <memory.h>
#define MAX 301

typedef struct node {
	int x;
	int y;
}	node;

int head, tail;
int map[MAX][MAX];
int count[MAX][MAX];

node que[MAX * MAX];

int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int t, l, n, m, a, b;

void	Enque(int x, int y)
{
	node tmp;
	tmp.x = x;
	tmp.y = y;
	que[tail] = tmp;
	tail = (tail + 1) % (MAX * MAX);
}

node	Deque(void)
{
	node tmp;
	tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return (tmp);
}

void	BFS(int x, int y)
{
	int nx, ny;
	int i;
	node tmp;

	Enque(x, y);
	count[x][y] = 0;
	while (head != tail)
	{
		tmp = Deque();
		i = 0;
		while (i < 8)
		{
			nx = tmp.x + dx[i];
			ny = tmp.y + dy[i];
			if (nx >= 0 && nx < l && ny >= 0 && ny < l && !count[nx][ny])
			{
				Enque(nx, ny);
				count[nx][ny] = count[tmp.x][tmp.y] + 1;
				if (nx == n && ny == m)
					return ;
			}
			i++;
		}
	}
}

int main(void)
{
	int i;

	scanf("%d", &t);
	i = 0;
	while (i < t)
	{
		memset(count, 0, sizeof(count));
		memset(que, 0, sizeof(que));
		head = 0;
		tail = 0;
		scanf("%d %d %d %d %d", &l, &a, &b, &n, &m);
		if (a == n && b == m)
			printf("0\n");
		else
		{
			BFS(a, b);
			printf("%d\n", count[n][m]);
		}
		i++;
	}
	return (0);
}