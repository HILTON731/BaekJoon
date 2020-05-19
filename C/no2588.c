#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	int num1,num2;
	int answer[4];
	scanf("%d",&num1);
	scanf("%d", &num2);
	answer[0] = num1 * (num2 % 10);
	answer[1] = num1 * ((num2 % 100 - num2 % 10) / 10);
	answer[2]= num1 * (num2 / 100);
	answer[3] = num1 * num2;
	for (int i = 0; i < 4; i++) {
		printf("%d\n", answer[i]);
	}
	return 0;
}