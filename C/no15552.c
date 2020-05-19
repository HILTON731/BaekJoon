#pragma warning(disable:4996)
#include<stdio.h>
int main() {
int test_case, num1, num2,i;
	scanf("%d", &test_case);
	for (i = 0; i < test_case; i++) {
		scanf("%d %d", &num1, &num2);
		printf("%d\n", num1 + num2);
		
	}
	getch();
	return 0;
}