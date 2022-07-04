#include <stdio.h>
#define MAX 5001

int count;
int sugar[MAX];
int n;

int main(void)
{
	sugar[0] = -1;
	sugar[1] = -1;
	sugar[2] = -1;
	sugar[3] = 1;
	sugar[5] = 1;
	sugar[4] = -1;

	scanf("%d", &n);
	for (int i = 6; i <= n; i++)
	{
		if (sugar[i - 3] == -1 && sugar[i - 5] == -1)
			sugar[i] = -1;
		else
		{
			if (sugar[i - 5] == -1)
				sugar[i] = sugar[i - 3] + 1;
			else if (sugar[i - 3] == -1)
				sugar[i] = sugar[i - 5] + 1;
			else if (sugar[i - 3] != -1 && sugar[i - 3] <= sugar[i - 5])
				sugar[i] = sugar[i - 3] + 1;
			else if (sugar[i - 5] != -1 && sugar[i - 5] <= sugar[i - 3])
				sugar[i] = sugar[i - 5] + 1;
		}
	}
	printf("%d\n", sugar[n]);
}