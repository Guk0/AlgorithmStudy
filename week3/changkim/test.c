#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[1][4];

	strcpy(a[0], "abc");
	if (a[0][1] == 'a')
		printf("ok\n");
	else
		printf("no\n");
}