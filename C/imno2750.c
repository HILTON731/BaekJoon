#pragma warning(disable:4996)
#include <stdio.h>
//insertion sort
/*
int main() {
	int num,i, j, k, a[1000],tmp;
	scanf("%d", &num);
	for (int t = 0; t < num; t++)
		scanf("%d", &a[t]);
	for (j = 1; j < num; j++) {
		i = 0;
		while (a[j] > a[i])i++;
		tmp = a[j];
		for (k = 0; k < j - i; k++)
			a[j - k] = a[j - k - 1];
		a[i] = tmp;
	}
	for (int t = 0; t < num; t++)
		printf("%d\n", a[t]);
	getch();
	return 0;
}
*/
//bubble sort
int main() {
	int num, tmp, a[1000];
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < num-1; i++)
		for (int j = 0; j < num - i-1; j++) {
			if (a[j] > a[j + 1]) {
				tmp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = tmp;
			}
		}
	for (int i = 0; i < num; i++)
		printf("%d\n", a[i]);
	getch();
	return 0;
}
				