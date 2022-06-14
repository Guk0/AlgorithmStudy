#include <stdio.h>
#define MAX 102

int n, m;
int connect[MAX][MAX];
int visit[MAX];

int que[MAX * MAX];
int head, tail, count;

int		Deque(void)
{
	int tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return tmp;
}

void	Enque(int x)
{
	que[tail] = x;
	tail = (tail + 1) % (MAX * MAX);
}

void	BFS()
{
	Enque(1);
	visit[1] = 1;
	while (head != tail)
	{
		int tmp = Deque();
		for (int i = 1; i <= n; i++)
		{
			if (connect[tmp][i] == 1 && visit[i] == 0)
			{
				Enque(i);
				visit[i] = 1;
				count++;
			}
		}
	}
}

int main(void)
{
	int a, b;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &a, &b);
		connect[a][b] = 1;
		connect[b][a] = 1;
	}
	BFS();
	printf("%d\n", count);
}