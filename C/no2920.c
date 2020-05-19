#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int main() {
	int a[8];
	int i, count = 0;
	for (int j = 0; j < 8; j++) {
		scanf("%d", &a[j]);
	}

	for (i = 0; i < 7; i++) {
		if (a[i + 1] - a[i] == 1) count++;
		else if (a[i + 1] - a[i] == -1) count--;
		printf("%d\n", count);

	}
	if (count == 7)printf("ascending\n");
	else if (count == -7)printf("descending\n");
	else printf("mixed\n");
	getch();
	return 0;
}