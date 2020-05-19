#pragma warning(disable:4996)
#include<stdio.h>
int a[3];
int i,j,k;
int main() {
	scanf("%d %d %d", &a[0], &a[1], &a[2]);
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 2; j++){
			if (a[j] > a[j + 1]) {
				k=a[j];
				a[j]=a[j+1];
				a[j+1]=k;
		}
		}
	}
	printf("%d", a[1]);
	getch();
	return 0;
}