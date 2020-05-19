#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	int line, stand, num,i;
	scanf("%d %d", &line, &stand);
	for (i = 0; i < line; i++) {
		scanf("%d", &num);
		if (stand > num) {
			printf("%d ", num);
		}
	}
	getch();
	return 0;
}