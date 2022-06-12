#include <stdio.h>
#define MAX 51

typedef struct node {
	int x;
	int y;
}	node;

int n, m, count;
char map[MAX][MAX];
int visit[MAX][MAX];

node que[MAX * MAX];
int head, tail;
int dy[4] = {1, 0, -1, 0};
int dx[4] = {0, -1, 0, 1};

node	Deque(void)
{
	node tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return tmp;
}

void	Enque(int x, int y)
{
	que[tail].x = x;
	que[tail].y = y;
	tail = (tail + 1) % (MAX * MAX);
}

void	BFS()
{
	int nx, ny;
	while (head != tail)
	{
		node tmp = Deque();
		if (map[tmp.x][tmp.y] == '-')
		{
			for (int i = 0; i < 4; i+=2)
			{
				nx = tmp.x + dx[i];
				ny = tmp.y + dy[i];
				if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == '-' && visit[nx][ny] != 1)
				{
					Enque(nx, ny);
					visit[nx][ny] = 1;
				}
			}
		}
		else if (map[tmp.x][tmp.y] == '|')
		{
			for (int i = 1; i < 4; i+=2)
			{
				nx = tmp.x + dx[i];
				ny = tmp.y + dy[i];
				if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == '|' && visit[nx][ny] != 1)
				{
					Enque(nx, ny);
					visit[nx][ny] = 1;
				}
			}
		}
	}
	count++;
}


int main(void)
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", map[i]);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (visit[i][j] != 1)
			{
				Enque(i, j);
				visit[i][j] = 1;
				BFS();
			}
		}
	}
	printf("%d\n", count);
}