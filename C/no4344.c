#pragma warning(disable:4996)
#include<stdio.h>
int main() {
	int test, num,count=0;
	double score[1000] = { 0, }, sum = 0, avg;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		scanf("%d", &num);
		for (int j = 0; j < num; j++) {
			scanf("%lf", &score[j]);
			sum += score[j];
		}
		avg= sum / num;
		for (int k = 0; k < num; k++) {
			if (score[k] > avg)
				count++;
		}
		printf("%.3lf%%\n", (double)count / (double)num * 100);
		sum = 0;
		count = 0;
	}
	getch();
	return 0;
}