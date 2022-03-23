#include <stdio.h>
#include <string.h>

// find Valid Parenthesis String

int	check(char *s)
{
	int	len;
	int	sum = 0;

	len = strlen(s);
	if (len % 2 == 1)
		return (2);
	for (int i = 0; i < len; i++)
	{
		if (sum < 0)
			return (3);
		if (s[i] == '(')
			sum += 1;
		else
			sum -= 1;
		if (i == len - 1 && sum != 0)
			return (4);

	}
	return (1);
}
// '('을 +1 로, ')'을 -1 로 치환해서 생각하면
// 배열 요소 처음부터 순서대로 더했을 때 한 번이라도 sum 값이 음수가 되지 않고
// 마지막 -1 을 더했을 때 sum 값이 0이 된다면 
// VPS(valid parenthesis string)이라고 볼 수 있다
// 처음부터 괄호의 개수가 짝수가 아니면 반복문을 시행하지 않는다
// vps 인 경우 1을, 아닌 경우 -1을 반환하도록 함수를 구성했다


int	main(void)
{
	int	T;
	char	PS[50]; // Parenthesis String

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%s", PS);
		if (check(PS) == 1)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return (0);
}
