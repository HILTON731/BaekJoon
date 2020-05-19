#pragma warning(disable:4996)
#include<stdio.h>
#define STUDENT 5
int main() {
	int score[STUDENT],sum=0,avg;

	for (int i = 0; i < STUDENT; i++) {
		scanf("%d", &score[i]);
	}
	for (int i = 0; i < STUDENT; i++) {
		if (score[i] < 40) {
			score[i] = 40;
			sum += 40;
		}
		else sum += score[i];
	}
	avg = sum / STUDENT;
	printf("%d\n", avg);
	getch();
	return 0;
}