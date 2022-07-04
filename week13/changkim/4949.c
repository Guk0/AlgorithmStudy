#include <stdio.h>
#include <string.h>
#include <unistd.h>


#define MAX 101

#define SMALL_IN '('
#define SMALL_OUT ')'
#define LARGE_IN '['
#define LARGE_OUT ']'


char stack[MAX];
int head;

void	push(char c)
{
	stack[head] = c;
	head = head + 1;
}

int main(void)
{
	int sign;

	sign = 0;
	while (1)
	{
		char str[101] = { 0 };
		int i = 0;
		memset(stack, 0, sizeof(stack));
		head = 0;
		scanf("%[^\n]s", str);
		if (str[0] == '.')
			break ;
		for (int j = 0; j < strlen(str); j++)
		{
			if (str[j] == LARGE_IN || str[j] == SMALL_IN)
				push(str[j]);
			else if (str[j] == LARGE_OUT)
			{
				if (stack[head - 1] == LARGE_IN)
				{
					if (head != 0)
						head -= 1;
					stack[head] = 0;
				}
				else
				{
					printf("no\n");
					break ;
				}
			}
			else if (str[j] == SMALL_OUT)
			{
				if (stack[head - 1] == SMALL_IN)
				{
					if (head != 0)
						head -= 1;
					stack[head] = 0;
				}
				else 
				{
					printf("no\n");
					break ;
				}
			}
			if (str[j] == '.')
			{
				if (head == 0)
					printf("yes\n");
				else
				{
					printf("no\n");
					break ;
				}
			}
		}
		getchar();
	}
	return (0);
}