#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define B 'B'
#define W 'W'

int count_arr[43][43] = { 0 };

void	ft_strncpy_ult(char **tmp, char **square, int x, int y)
{
	int i = 0, j = 0;
	
	while (j < 8)
	{
		i = 0;
		while (i < 8)
		{
			tmp[j][i] = square[y + j][x + i];
			i++;
		}
		tmp[j][i] = 0;
		j++;
	}
	tmp[j] = 0;
}

int	change_to_W(char *square, int idx)
{
	if (square[idx] == B)
	{
		square[idx] = W;
		return (1);
	}
	return (0);
}

int	change_to_B(char *square, int idx)
{
	if (square[idx] == W)
	{
		square[idx] = B;
		return (1);
	}
	return (0);
}

int	make_chess_count_W(char **tmp)
{
	int count_W = 0, x = 0, y = 0;

	while (y < 8)
	{
		x = 0;
		while (x < 8)
		{
			if (y == 0 && x == 0)
			{
				if (tmp[0][0] == B)
					count_W++;
				x = 1;
				while (x < 8)
				{
					count_W += change_to_B(tmp[0], x);
					x++;
					if (x == 8)
						break ;
					count_W += change_to_W(tmp[0], x);
					x++;
				}
				x = 0;
				y = 1;
			}
			if (y % 2 == 1)
			{
				count_W += change_to_B(tmp[y], x);
				x++;
				count_W += change_to_W(tmp[y], x);
				x++;
			}
			else
			{
				count_W += change_to_W(tmp[y], x);
				x++;
				count_W += change_to_B(tmp[y], x);
				x++;
			}
		}
		y++;
	}
	return (count_W);
}

int	make_result(int **count_arr, int n, int m)
{
	int i, j;

	i = 0;
	j = 0;
	int result = count_arr[0][0];
	while (i <  m - 6)
	{
		j = 0;
		while (j < n - 6)
		{
			result = count_arr[i][j] > count_arr[i][j + 1] ? count_arr[i][j + 1] : count_arr[i][j];
			j++;
		}
		i++;
	}
	return (result);
}

int	make_chess_count_B(char **tmp)
{
	int x = 0, y = 0, count_B = 0;

	while (y < 8)
	{
		x = 0;
		while (x < 8)
		{
			if (y == 0 && x == 0)
			{
				if (tmp[0][0] == W)
					count_B++;
				x = 1;
				while (x < 8)
				{
					count_B += change_to_W(tmp[0], x);
					x++;
					if (x == 8)
						break ;
					count_B += change_to_B(tmp[0], x);
					x++;
				}
				x = 0;
				y = 1;
			}
			if (y % 2 == 1)
			{
				count_B += change_to_W(tmp[y], x);
				x++;
				count_B += change_to_B(tmp[y], x);
				x++;
			}
			else
			{
				count_B += change_to_B(tmp[y], x);
				x++;
				count_B += change_to_W(tmp[y], x);
				x++;
			}
		}
		y++;
	}
	return (count_B);
}

int main(void)
{
	int m, n, x, y;
	char **square;
	char **tmp;

	scanf("%d%d", &m, &n);
	square = (char **)calloc(sizeof(char *), (m + 1));
	tmp = (char **)calloc(sizeof(char *), 9);
	int i = 0;
	while (i < 8)
	{
		tmp[i] = (char *)calloc(1, 9);
		i++;
	}
	y = 0;
	while (y < m)
	{
		square[y] = (char *)calloc(1, (n + 1));
		scanf("%s", square[y]);
		y++;
	}
	y = 0;
	int count_W = 0, count_B = 0;
	while (y < m - 7)
	{
		x = 0;
		while (x < n - 7)
		{
			ft_strncpy_ult(tmp, square, x, y);
			count_W = make_chess_count_W(tmp);
			ft_strncpy_ult(tmp, square, x, y);
			count_B = make_chess_count_B(tmp);
			count_arr[y][x] = count_W > count_B ? count_B : count_W;
			x++;
		}
		y++;
	}
	i = 0;
	int j = 0;
	int result = count_arr[0][0];
	while (i <  m - 7)
	{
		j = 0;
		while (j < n - 7)
		{
			result = result > count_arr[i][j] ? count_arr[i][j] : result;
			j++;
		}
		i++;
	}
	printf("%d", result);
}