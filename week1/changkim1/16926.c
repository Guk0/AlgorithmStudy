#include <stdlib.h>
#include <stdio.h>

#define min(a, b) (a < b ? a : b)

typedef struct result {
	int f_x;
	int f_y;
}	results;


int M, N, R;


int	circle_num(int x, int y)
{
	int circle, i, j;

	if (M % 2 == 0)
		i = x > (M / 2) - 1 ? M - 1 - x : x;
	else
		i = x > (M / 2) ? M - 1 - x : x;
	if (N % 2 == 0)
		j = y > (N / 2) - 1 ? N - 1 - y : y;
	else
		j = y > (N / 2) ? N - 1 - y : y;
	circle = min(i, j);
	return (circle);
}

results move_coo(int x, int y)
{
	results result;
	int circle, r_x, r_y, count;

	r_x = x, r_y = y;
	circle = circle_num(x, y);
	count = R % (2 * (M + N - (circle * 4)) - 4);
	while (count > 0)
	{
		if (r_x > circle && r_y == circle)
			r_x--;
		else if (r_x == circle && r_y < N - 1 - circle)
			r_y++;
		else if (r_x < M - 1 - circle && r_y == N - 1 - circle)
			r_x++;
		else if (r_x == M - 1 - circle && r_y > circle)
			r_y--;
		count--;
	}
	result.f_x = r_x;
	result.f_y = r_y;
	return (result);
}

int main(void)
{
	results f_c;
	int x = 0;
	int y = 0;
	int proto[300][300] = { 0 }, final[300][300] = { 0 };

	scanf("%d%d%d", &N, &M, &R);
	while (y < N)
	{
		x = 0;
		while (x < M)
		{
			scanf("%d", &proto[y][x]);
			x++;
		}
		y++;
	}
	y = 0;
	while (y < N)
	{
		x = 0;
		while (x < M)
		{
			f_c = move_coo(x, y);
			final[f_c.f_y][f_c.f_x] = proto[y][x];
			x++;
		}
		y++;
	}
	y = 0;
	while (y < N)
	{
		x = 0;
		while (x < M)
		{
			printf("%d ", final[y][x]);
			x++;
		}
		printf("\n");
		y++;
	}
}