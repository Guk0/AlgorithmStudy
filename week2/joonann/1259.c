#include <stdio.h>
#include <stdlib.h> //itoa 함수가 들어있는 헤더파일
                    // itoa 는 C표준이 아니라서 sprintf 함수를 이용해야 한다
#include <string.h>

int	main(void)
{
	char	str[6];
	int	N;
	int	len;
	int	yes_no;

	while (1)
	{
		scanf("%d", &N);
		if (N == 0)
			break ;
		sprintf(str, "%d", N); // 배열에 10진수 숫자인 문자열로 바꿔서 저장한다
		
		len = strlen(str);
		yes_no = 1;
		for (int i = 0; i < (len / 2); i++)
		{
			if (str[i] != str[len - 1 - i])
			{
				yes_no = 0;
				break ;
			}
		}
		if (yes_no == 1)
			printf("yes\n");
		else
			printf("no\n");
	}

	return (0);
}
