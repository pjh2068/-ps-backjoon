#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int array[9];
	int i = 0; int j=0;
	for (i; i < 9; i++)
	{
		int a;
		scanf("%d", &a);
		array[i] = a;
	}
	int max = array[0];
	int maindex = 0;
	for (j; j < 9 ; j++)
	{
		if (array[j] > max)
		{
			max = array[j];
			maindex = j;
		}
	}
	printf("%d\n", max);
	printf("%d", maindex+1);

	return 0;
}