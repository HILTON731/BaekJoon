#pragma warning (disable:4996)
#include<stdio.h>
#include<string.h>
#define MAX_TERM 80
void main() {
	int num, count, i, sum,j;
	char tmp[MAX_TERM];
	scanf("%d", &num);
	
	for (i = 0; i < num; i++) {
		scanf("%s", tmp);
		count = 0; sum = 0; j = 0;
		while (j<strlen(tmp)) {
			if (tmp[j] == 'O') {
				count++;
				sum += count;
				//printf("%d %d tmp\n", sum, count);
			}
			else {
				count = 0;
			}
			j++;
		}
		printf("%d\n", sum);
	}
	getch();
}