#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//#include <stdlib.h> //malloc,free 함수 들어가있음

int main(void)
{
	int array[1000000];
	int cnt; int i = 0; int j = 0;
	scanf("%d", &cnt);
	
	//int* array = (int*)malloc(sizeof(int)*cnt); 
	//* cnt에서 입력받은 만큼 배열 할당 가능
	//* int array[1000000]; 대체 가능
	
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
	
	//free(array);
	//* 동적할당 받은 array변수 deallocate
	
	return 0;
}
