#include <stdio.h>
#include <memory.h>
#define MAX 1001

int n, m, v, count;

int connect[MAX][MAX];
int visit[MAX];

int que[MAX * MAX];
int head, tail;

void	Enque(int x)
{
	que[tail] = x;
	tail = (tail + 1) % (MAX * MAX);
}

int		Deque(void)
{
	int tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return tmp;
}

void	BFS(void)
{
	Enque(v);
	visit[v] = 1;
	while (head != tail)
	{
		int tmp = Deque();
		printf("%d ", tmp);
		for (int i = 1; i <= n; i++)
		{
			if (connect[tmp][i] == 1 && visit[i] == 0)
			{
				Enque(i);
				visit[i] = 1;
			}
		}
	}
}

void	DFS(int x)
{
	int tmp;
	printf("%d ", x);
	visit[x] = 1;
	for (int i = 1; i <= n; i++)
	{
		if (connect[x][i] == 1)
		{
			tmp = i;
			if (visit[tmp] == 0)
				DFS(tmp);
		}
	}
}

int main(void)
{
	int a, b;
	scanf("%d %d %d", &n, &m, &v);
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);
		connect[a][b] = 1;
		connect[b][a] = 1;
	}
	DFS(v);
	memset(visit, 0, sizeof(visit));
	printf("\n");
	BFS();
}