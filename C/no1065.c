#pragma warning(disable:4996)
#include<stdio.h>
int dn(int a) {
	int div, tmp[4] = { 0, },count=0;
	div = a;
	if (div < 100) {
		count = 1;
		return count;
	}
	else if (div < 1000) {
		for (int i = 0; i < 4; i++) {

			tmp[i] = div % 10;
			div /= 10;
		}
		count=((tmp[2] - tmp[1]) == (tmp[1] - tmp[0])) ? 1 : 0;
				}

	return count;
	}

int main() {
	int num,tmp,sum=0;
	
	scanf("%d", &num);
	for (int i = 1; i <= num; i++) {
		tmp = dn(i);
		if (tmp !=0) {
			sum++;
		}
	}
	printf("%d\n", sum);
	getch();
	return 0;
}
/*
#include<stdio.h>
int main() {
	int n, i, k, t, a[3], han;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		if (i < 100)han = i;
		else if (i == 1000)break;
		else {
			k = 0; t = i;
			while (t > 0) {
				a[k] = t % 10;
				t /= 10; k++;
			}
			if (a[0] - a[1] == a[1] - a[2])
				han++;
		}
	}
	printf("%d", han);
	getch();
	return 0;
}*/