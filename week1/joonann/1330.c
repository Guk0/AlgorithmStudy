#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int	main(void)
{
	int	A, B;

	scanf("%d %d", &A, &B);
	if (A > B)
		printf("%c", '>');
	else if (A < B)
		printf("%c", '<');
	else
		printf("%c%c", '=', '=');
	return (0);
}