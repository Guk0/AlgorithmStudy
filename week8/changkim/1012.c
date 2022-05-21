#include <stdio.h>
#include <memory.h>
#define M  51

int w, h, t;
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

void	BFS()
{
	int nx, ny;

	while (is_empty())
	{
		node tmp;
		tmp = Deque();
		for (int i = 0; i < 4; i++)
		{
			
		}
	}
}