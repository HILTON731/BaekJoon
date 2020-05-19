#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	int num, count = 0, sum, renew,temp,a,b;
	scanf("%d", &num);
	temp = num;
	while (1) {
		a = temp / 10;
		b = temp % 10;
		sum = a + b;
		renew = (sum%10) + (b * 10);
		count++;
		if (renew == num) {
			printf("%d", count);
			break;
		}
		temp = renew;
	}
	getch();
	return 0;
}