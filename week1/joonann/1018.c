#include <stdio.h>
#include <stdlib.h>
#define _CRT_SECURE_NO_WARNINGS

static char *chess_wb = "WBWBWBWB";
static char *chess_bw = "BWBWBWBW";
// 만들어야하는 체스판은 번갈아서 두 패턴만 나오기 때문에 
// 최소한의 배열만 선언해준다

int	count_one_line(char *board_line, const char *chess)
{
	int	result = 0;

	for (int i = 0; i < 8; i++)
	{
		if (board_line[i] != chess[i])
			result++;
	}
	return (result);
}
// chess 배열과 한 줄씩 비교해 색깔이 다른 정사각형의 개수를 세어주는 함수

int	paint_count(char **board, int N_cord, int M_cord, int result)
{
	int	temp_w = 0;
	int	temp_b = 0;

	for (int i = 0; i < 4; i++)
	{
		if (result < temp_w)
			break ;
		temp_w += count_one_line(board[N_cord + (i * 2)] + M_cord, chess_wb);
		temp_w += count_one_line(board[N_cord + (i * 2) + 1] + M_cord, chess_bw);
	}
	for (int i = 0; i < 4; i++)
	{
		if (result < temp_b)
			break ;
		temp_b += count_one_line(board[N_cord + (i * 2)] + M_cord, chess_bw);
		temp_b += count_one_line(board[N_cord + (i * 2) + 1] + M_cord, chess_wb);
	}
	return (temp_w < temp_b ? temp_w : temp_b);
}
// 한 지점에서 체스 보드가 시작했을 때 색칠해야 되는 정사각형 개수의  최솟값을 구하는 함수
// 이전 결과값도 매개변수로 받아와서
// 이전 결과값보다 구하는 값이 커지면 바로 -1 반환하고 반복문 종료
// chess_wb와 chess_bw를 번갈아 확인해준 결과값을 더해준다.
// 검은색으로 시작하는 경우와 흰색으로 시작하는 경우 둘 다 계산해서 값이 작은 쪽을  반환

int	main(void)
{
	int	N, M, result, temp;
	char	**board;

	scanf("%d %d\n", &N, &M);
	board = (char **)malloc(sizeof(char *) * (N + 1)); 
	for (int i = 0; i < N; i++)
	{
		board[i] = (char *)malloc(sizeof(char) * (M + 1));
		scanf("%s", board[i]);
	}	
	board[N] = NULL;
	
// 2차원 배열 선언 후 표준입력으로 받은 보드를 2차원 배열에 저장한다

	result = paint_count(board, 0, 0, 65); // 결과값의 최대값은 64이므로 그것보다 큰 값을 파라미터로 넘겨줌
	temp = 0;
	
	for (int i = 0; i <= N - 8; i++)
	{
		for (int j = 0; j <= M - 8; j++)
		{
			temp = paint_count(board, i, j, result);
			if (temp < result)
				result = temp;
		}
	}
	printf("%d", result);
		
	for (int i = 0; i <= N; i++)
		free(board[i]);
	free(board);
	return (0);

}
