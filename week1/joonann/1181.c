#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int	N;

typedef struct word_t {
	char	*word;
	int	word_len;
} word;
// 구조체를 선언해준다. 구조체 멤버는 입력받을 단어와 단어의 길이


void	swap(word *word1, word *word2)
{
	word	tmp;
	tmp = *word1;
	*word1 = *word2;
	*word2 = tmp;
}
// 구조체 두 개의 주소값을 매개변수로 받아와 두 구조체의 순서를 뒤바꿔주는 함수

void	arrange(word **arr)
{
	word tmp;

	for (int i = 0; i + 1 < N; i++)
	{
		for (int j = 1; i + j < N; j++)
		{
			if ((*arr)[i].word_len > (*arr)[i + j].word_len)
				swap(&(*arr)[i], &(*arr)[i + j]);
			else if ((*arr)[i].word_len < (*arr)[i + j].word_len)
				continue ;
			else
				if (strncmp((*arr)[i].word, (*arr)[i + j].word, (*arr)[i].word_len) > 0)
					swap(&(*arr)[i], &(*arr)[i + j]);
		}
	}
}
// 구조체 멤버 중 단어 길이를 기준으로 구조체들을 정렬하는 함수 (버블정렬을 이용했다)
// 길이가 같은 경우 strncmp 함수를 통해 사전순으로 정렬해준다

int	main(void)
{
	char	tmp[50];
	int	tmp_len;

	scanf("%d", &N);
	word	*arr;

	arr = (word *)malloc(sizeof(word) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%s", tmp);
		tmp_len = strlen(tmp);
		arr[i].word = (char *)malloc(sizeof(char) * (tmp_len + 1));
		strncpy(arr[i].word, tmp, tmp_len);
		arr[i].word_len = tmp_len;
	}

	arrange(&arr);
	
	printf("%s\n", arr[0].word);
	for (int i = 1; i < N; i++)
	{
		if (strncmp(arr[i].word, arr[i - 1].word, arr[i].word_len) == 0)
			continue ;
		printf("%s\n", arr[i].word);
	}

	for (int i = 0; i < N; i++)
		free(arr[i].word);
	free(arr);
}
// 구조체 멤버들을 main함수 내에서 동적할당 후 저장하고 마지막에 메모리 해제까지 해준다
