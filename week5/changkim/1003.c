#include <stdio.h>
#include <stdlib.h>

#define MAX 40
typedef struct	fib {
	int one;
	int zero;
}	fibo;

int main(void)
{
	int n;
	int i;
	int num;
	fibo fib_set[MAX];

	scanf("%d", &n);
	i = 0;
	fib_set[0].one = 0;
	fib_set[0].zero = 1;
	fib_set[1].one = 1;
	fib_set[1].zero = 0;
	i = 2;
	while (i <= MAX)
	{
		fib_set[i].one = fib_set[i - 2].one + fib_set[i - 1].one;
		fib_set[i].zero = fib_set[i - 2].zero + fib_set[i - 1].zero;
		i++;
	}
	i = 0;
	while (i < n)
	{
		scanf("%d", &num);
		printf("%d %d\n", fib_set[num].zero, fib_set[num].one);
		i++;
	}
}