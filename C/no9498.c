#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	int i=0;
	scanf("%d", &i);
	if ((i >= 90) && (i <= 100)) {
		printf("A\n");
	}
	else if (i >= 80) {
		printf("B\n");
	}
	else if (i >= 70) {
		printf("C\n");
	}
	else if (i >= 60) {
		printf("D\n");
	}
	else {
		printf("F\n");
	}

	getch();
	return 0;
}