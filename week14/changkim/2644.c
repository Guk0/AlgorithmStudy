#include <stdio.h>
#include <memory.h>

#define MAX 101

int visit[MAX];
int	map[MAX][MAX];
int level[MAX];

int que[MAX * MAX];
int head, tail;

int n, m, a, b;
int x, y;

int	Deque()
{
	int tmp;
	tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return (tmp);
}

void	Enque(int q)
{
	que[tail] = q;
	tail = (tail + 1) % (MAX * MAX);
}

int	BFS()
{
	int count = 1;

	while (head != tail)
	{
		int tmp = Deque();
		if (tmp == b)
			return (level[b]);
		for (int i = 1; i <= n; i++)
		{
			if (map[tmp][i] == 1 && visit[i] == 0)
			{
				level[i] = level[tmp] + 1;
				Enque(i);
				visit[i] = 1;
			}
		}
	}
	return (-1);
}

int main(void)
{
	int ans;

	scanf("%d %d %d %d", &n, &a, &b, &m);
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &x, &y);
		map[x][y] = 1;
		map[y][x] = 1;
	}
	level[a] = 0;
	Enque(a);
	visit[a] = 1;
	ans = BFS();
	printf("%d\n", ans);
}