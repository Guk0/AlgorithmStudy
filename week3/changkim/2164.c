#include <stdlib.h>
#include <stdio.h>

int arr[1000000];

int main(void)
{
	int back, front, i;

	scanf("%d", &back);
	front = 0;
	i = 0;
	while (i < back)
	{
		arr[i] = i + 1;
		i++;
	}
	if (back == 1)
		printf("1");
	back--;
	while (front != back)
	{
		arr[front] = 0;
		front++;
		if (front == back)
		{
			printf("%d", arr[front]);
			return (0);
		}
		back++;
		arr[back] = arr[front];
		arr[front] = 0;
		front++;
	}
}