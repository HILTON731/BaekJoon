#pragma warning(disable:4996)
#include <stdio.h>
int main() {
	int A, B;
	double avg;
	scanf("%d %d", &A, &B);
	avg = (double)A / B;
	printf("%.9f", avg);
	getch();
	return 0;
}