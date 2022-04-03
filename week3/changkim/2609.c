#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX 10000
int n_[MAX];
int m_[MAX];
int yak = 1;
int bae = 1;

int main(void)
{
	int n, m;
	int i;
	int max;

	i = 2;
	scanf("%d%d", &n, &m);
	max = n > m ? n : m;
	while (i <= max)
	{
		while (n % i == 0 && n != 1)
		{
			n_[i]++;
			n /= i;
		}
		while (m % i == 0 && m != 1)
		{
			m_[i]++;
			m /= i;
		}
		if (m == 1 && n == 1)
			break ;
		i++;
	}
	i = 2;
	while (i <= max)
	{
		if (n_[i] != 0 && m_[i] != 0)
		{
			yak *= n_[i] < m_[i] ? pow(i, n_[i]) : pow(i, m_[i]);
		}
		if (n_[i] != 0 || m_[i] != 0)
		{
			bae *= n_[i] > m_[i] ? pow(i, n_[i]) : pow(i, m_[i]);
		}
		i++;
	}
	printf("%d\n%d", yak, bae);
}