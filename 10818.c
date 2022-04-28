#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int array[1000000];
	int cnt; int i = 0; int j = 0;
	scanf("%d", &cnt);
	for (i; i < cnt; i++)
	{
		int a;
		scanf("%d", &a);
		array[i] = a;
	}
	int max = array[0];
	int min = array[0];
	for (j; j < cnt; j++)
	{
		if (array[j] > max)
			max = array[j];
		else if (array[j] < min)
			min = array[j];
	}
	printf("%d %d", min, max);

	return 0;
}