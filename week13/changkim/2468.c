#include <stdio.h>
#include <memory.h>

#define MAX 101

typedef struct node {
	int x;
	int y;
}	node;

node	que[MAX * MAX];
int 	head, tail;

int		map[MAX][MAX];
int		visit[MAX][MAX];
int		sink[MAX][MAX];
int		n;
int		count;

int		dx[4] = {1, 0, -1, 0};
int		dy[4] = {0, -1, 0, 1};

node	Deque()
{
	node tmp;

	tmp.x = que[tail].x;
	tmp.y = que[tail].y;
	tail = (tail + 1) % (MAX * MAX);
	return (tmp);	
}

void	Enque(int x, int y)
{
	que[head].x = x;
	que[head].y = y;
	head = (head + 1) % (MAX * MAX);
}

void	BFS()
{
	int	nx;
	int	ny;
	node tmp;

	while (head != tail)
	{
		tmp = Deque();
		for (int i = 0; i < 4; i++)
		{
			nx = tmp.x + dx[i];
			ny = tmp.y + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < n)
			{
				if (sink[nx][ny] != 0 && visit[nx][ny] == 0)
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
	int ans;
	int max;
	int idx;

	ans = 0;
	max = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &map[i][j]);
			if (map[i][j] > max)
			max = map[i][j];
		}
	}
	for (int i = 0; i < max; i++)
	{
		memset(sink, 0, sizeof(sink));
		memset(que, 0, sizeof(que));
		memset(visit, 0, sizeof(visit));
		count = 0;
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				if (map[j][k] > i)
					sink[j][k] = 1;
			}
		}
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				if (visit[j][k] == 0 && sink[j][k] == 1)
				{
					Enque(j, k);
					visit[j][k] == 1;
					BFS();
				}
			}
		}
		if (ans < count)
			ans = count;	
	}
	printf("%d\n", ans);
}