#include <stdio.h>
#define MAX 51

char str[MAX];
int len;
unsigned long long res[MAX];
unsigned long long ans;

int main(void)
{
	scanf("%d", &len);
	scanf("%s", str);

	for (int i = 0; i < len; i++)
	{
		res[i] += str[i] - 'a' + 1;
		for (int j = 0; j < i; j++)
		{
			res[i] *= 31;
			res[i] = res[i] % 1234567891;
		}
	}
	for (int i = 0; i < len; i++)
		ans += res[i];
	printf("%lld\n", ans % 1234567891);
}