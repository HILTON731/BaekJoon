#pragma warning (disable:4996)
#include <stdio.h>
int main() {
	int num1, num2, num3;
	int sum1, sum2, sum3,sum4;
	scanf("%d %d %d", &num1, &num2, &num3);
	sum1 = (num1 + num2) % num3;
	sum2 = (num1 % num3 + num2 % num3) % num3;
	sum3 = (num1 * num2) % num3;
	sum4 = (num1 % num3 * num2 % num3) % num3;
	printf("%d\n%d\n%d\n%d\n", sum1, sum2, sum3, sum4);
	return 0;
}