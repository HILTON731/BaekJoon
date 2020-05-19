#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	double test, score, best=0,change=0;
	double avg;
	scanf("%lf", &test);
	for (int i = 0; i < test; i++) {
		scanf("%lf", &score);
		if (score > best) {
			best = score;
		}
		change += score;

	}
	avg = change / (best*test) * 100;
	printf("%.2lf", avg);
	getch();
	return 0;
}