#pragma warning(disable:4996)
#define MAX_NUM 1000001
#include<stdio.h>
#include<string.h>

int main() {
	char arr[MAX_NUM];
	int i, count = 0;
	fgets(arr, sizeof(arr) - 1, stdin);
	

	for (i = 0; arr[i+1]; i++) {
		if (arr[i] == ' ' && (arr[i + 1] != '\n'))
				count++;
	}
	if (arr[0] == ' ')
		count--;
//	if (arr[strlen(arr)-2] == ' ')
	//	count--;
	printf("%d\n", ++count);
	getch();
	return 0;
}
/*
int main()
{
	char arr[MAX_NUM];
	int i = 1;
	int count = 0;
	fgets(arr, sizeof(arr) - 1, stdin);
	arr[strlen(arr) - 1] = '\0';
	while (arr[i + 1]) {
		if (arr[i] == ' ') {
			if ((arr[i - 1] != ' ') && (arr[i + 1] != ' '))
				count++;
		}
		i++;
	}
	if (strlen(arr) == 1 && arr[0] == ' ')
		count--;
	printf("%d\n", ++count);
	getch();
	return 0;
}*/