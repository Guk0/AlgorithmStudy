#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

struct node {
	int x;
	int y;
};

struct node queue[2500];
int head = 0;
int tail = 0;

void	Enque(int x, int y)
{
	struct node tmp;
	tmp.x = x;
	tmp.y = y;
	queue[tail] = tmp;
	tail = (tail + 1) % 2500;
}

struct node	Deque(void)
{
	struct node tmp;
	tmp = queue[head];
	head = (head + 1) % 2500;
	return (tmp);
}

int	Is_Empty()
{
	if (head == tail)
		return (0);
	else
		return (1);
}

int	dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

int	Is_visited[51][51];
int input[51][51];
int w;
int h;

void BFS(void)
{
	int next_X;
	int next_Y;
	int i;

	while (Is_Empty() == 1)
	{
		struct node tmp = Deque();
		i = 0;
		while (i < 8)
		{
			next_X = tmp.x + dx[i];
			next_Y = tmp.y + dy[i];
			if (0 <= next_X && next_X < h && next_Y < w && 0 <= next_Y)
			{
				if (!Is_visited[next_X][next_Y] && input[next_X][next_Y])
				{
					Enque(next_X, next_Y);
					Is_visited[next_X][next_Y] = 1;
				}
			}
			i++;
		}
	}
}

int main(void)
{
	while (1)
	{
		scanf("%d %d", &w, &h);
		if (w == 0 && h == 0)
			return (0);
		int count = 0;
		memset(Is_visited, 0, sizeof(Is_visited));
		memset(input, 0, sizeof(input));
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
				scanf("%d", &input[i][j]);
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (!Is_visited[i][j] && input[i][j])
				{
					Enque(i, j);
					Is_visited[i][j] = 1;
					BFS();
					count++;
				}
			}
		}
		printf("%d\n", count);
	}
	return (0);
}