#include <stdio.h>
#include <memory.h>
#define MAX 51

int visited[MAX][MAX];
int input[MAX][MAX];
int w, h, count;
int head, tail;
int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

struct node {
	int x;
	int y;
};

struct node que[2500];

void Enque(int x, int y)
{
	struct node tmp;
	tmp.x = x;
	tmp.y = y;
	que[tail] = tmp;
	tail = (tail + 1) % 2500;
}

struct node Deque(void)
{
	struct node tmp;
	tmp = que[head];
	head = (head + 1) % 2500;
	return (tmp);
}

int Is_empty()
{
	if (head == tail)
		return (0);
	else
		return (1);
}

void	BFS(void)
{
	int n_x;
	int n_y;

	while (Is_empty())
	{
		int i = 0;
		struct node tmp = Deque();
		while (i < 8)
		{
			n_x = tmp.x + dx[i];
			n_y = tmp.y + dy[i];
			if (n_x >= 0 && n_x < h && n_y >= 0 && n_y < w)
			{
				if (!visited[n_x][n_y] && input[n_x][n_y])
				{
					Enque(n_x, n_y);
					visited[n_x][n_y] = 1;
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
		count = 0;
		scanf("%d %d", &w, &h);
		if (w == 0 && h == 0)
			return (0);
		memset(visited, 0, sizeof(visited));
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
				if (!visited[i][j] && input[i][j])
				{
					Enque(i, j);
					visited[i][j] = 1;
					BFS();
					count++;
				}
			}
		}
		printf("%d\n", count);
	}
}