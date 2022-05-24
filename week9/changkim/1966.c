#include <stdio.h>
#include <memory.h>
#define MAX 101

typedef struct node {
	int res;
	int imp;
}	node;

int head, tail, count;
int t, n, m;

node	que[MAX * MAX];
node	input[MAX];

void	Enque(node input)
{
	que[tail] = input;
	tail = (tail + 1) % (MAX * MAX);
}

node	Deque(void)
{
	node tmp;
	tmp = que[head];
	head = (head + 1) % (MAX * MAX);
	return (tmp);
}

int	is_there_bigger_one()
{
	int i;

	i = head + 1;
	while (i < tail)
	{
		if (que[head].imp < que[i].imp)
			return (1);
		i++;
	}
	return (0);
}

int main(void)
{
	int i, j;

	i = 0;
	scanf("%d", &t);
	while (i < t)
	{
		j = 0;
		count = 0;
		node tmp;
		head = 0;
		tail = 0;
		memset(input, 0, sizeof(input));
		memset(que, 0, sizeof(que));
		scanf("%d %d", &n, &m);
		input[m].res = 1;
		while (j < n)
		{
			scanf("%d", &input[j].imp);
			Enque(input[j]);
			j++;
		}
		while (head != tail)
		{
			if (is_there_bigger_one())
			{
				tmp = Deque();
				Enque(tmp);
			}
			else
			{
				tmp = Deque();
				count++;
				if (tmp.res == 1)
				{
					printf("%d\n", count);
					break ;
				}
			}
		}
		i++;
	}
	return (0);
}