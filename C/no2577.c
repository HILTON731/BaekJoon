#pragma warning(disable:4996)
#include<stdio.h>
#define MAX_SIZE 100
int main() {
	int A, B, C, mul, count[10] = {0,};
	scanf("%d %d %d", &A, &B, &C);
	mul = A * B * C;
	while (mul> 0) {
		count[mul % 10]++;
		mul /= 10;
	}

	for (int j = 0; j < 10; j++)
		printf("%d\n", count[j]);
	getch();
	return 0;
}