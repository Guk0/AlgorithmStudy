#include <stdio.h>
#include <stdlib.h>

#define MIN(X, Y) ((X) <= (Y) ? (X) : (Y))

void	print_arr(int **arr, int N, int M)
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			printf("%d", arr[i][j]);
			if (j != M - 1)
				printf(" "); // 중간 띄어쓰기 출력 조건식
			else
				printf("\n");
		}
	}
	return ;
}
// 2차원 배열을 Aij 인덱스 순서대로 출력하는 함수

int	tmp_index(int **arr, int N, int M, int i, int tmp_index)
{
	int size_N = N - (i * 2);
	int size_M = M - (i * 2);

	if (tmp_index < size_N) // tmp_index = 0 ~ 3 왼쪽 
		return (arr[i + tmp_index][i]);
	if (tmp_index >= size_N && tmp_index < size_N + size_M - 1) // tmp_index = 4 ~ 6 아래
		return (arr[N - i - 1][i + (tmp_index - size_N + 1)]);
	if (tmp_index >= size_N + size_M - 1 && tmp_index < (size_N * 2) + size_M - 2) // tmp_index 7 ~ 9 오른쪽
		return (arr[N - i - 1 - (tmp_index - (size_N + size_M - 2))][M - i - 1]);
	else // tmp_index 10 ~ 11 위
		return (arr[i][M - i - 1 - (tmp_index - ((size_N * 2) + size_M - 2) + 1)]);
}

// 시작하는 지점은 arr[i][i] ~ 마지막 지점 arr[N - i - 1][M - i - 1]


void	rotate(int ***arr, int N, int M, int R)
{
	int *tmp;
	int size;

	for (int i = 0; i < ((N <= M ? N : M) / 2); i++)
	{
		size = ((N - (i * 2)) * 2) + ((M - (i * 2) - 2) * 2); // 옮겨줄 배열의 사이즈
		tmp = (int *)malloc(sizeof(int) * size);
		for (int j = 0; j < size; j++)
			tmp[j] = tmp_index((*arr), N, M, i, j);
		for (int k = 0; k < N - (i * 2); k++)
		{
			int start_point = size - (R % size);
			(*arr)[i + k][i] = tmp[(start_point + k) % size];
			(*arr)[N - i - 1 - k][M - i - 1] = tmp[(start_point + (size / 2) + k) % size];
		}
		for (int k = 0; k < M - (i * 2) - 2; k++)
		{
			int start_point = size - (R % size) + (N - (i * 2));
			(*arr)[N - i - 1][i + 1 + k] = tmp[(start_point + k) % size];
			(*arr)[i][M - i - 2 - k] = tmp[(start_point + (size / 2) + k) % size];
		}
		// start_point, start_point + (size / 2) 값을 인덱스로 갖는 tmp 배열의 요소부터
		// 차례대로 인덱스 값에 1씩 추가한 요소들을 이용해 왼쪽과 오른쪽 열 완성
		// start_point + (size / 4) + 1, start_point + (size / 4 * 3) 값을 인덱스로 갖는 tmp 배열의 요소부터
		// 차례대로 인덱스 값에 1씩 추가한 요소들을 이용해 위와 아래 행 완성

		free(tmp);
	}
}


int	main(void)
{
	int	N, M, R;
	int	**arr;

	scanf("%d %d %d", &N, &M, &R);
	arr = (int **)malloc(sizeof(int *) * N);
	for (int i = 0; i < N; i++)
		arr[i] = (int *)malloc(sizeof(int) * M);
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		scanf("%d", &(arr[i][j]));
	}
	rotate(&arr, N, M, R);
	print_arr(arr, N, M);

	for (int i = 0; i < N; i ++)
		free((void *)arr[i]);
	free(arr);

}

// 변수들을 선언한 int형 변수 N, M, R에 저장, 
// 2차원 배열을 선언해서 입력받은 숫자들을 2차원 배열에 저장한다.
