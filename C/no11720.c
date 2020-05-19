#pragma warning(disable:4996)
/*
#include<stdio.h>
int NUM1,i;
static int SUM_RAND = 0;
int NUM_RAND[101];
int main() {
	scanf("%d", &NUM1);
	for (i = 0; i < NUM1; i++) {
		scanf("%d",&NUM_RAND[i]);
		SUM_RAND += (int)NUM_RAND[i];
	}
	printf("%d", SUM_RAND);
	getch();
	return 0;
}
*/
//같은 숫자 입력시 프로그램 정상작동 안함;; get때도 마찬가지
/*
#include<stdio.h>
#include<stdlib.h>
int main(){
	int n, sum = 0;
	scanf("%d", &n);
	char *num = (char*)malloc(sizeof(char)*n);
	for (int i = n; i >= 0; i--) {
		scanf("%c", &num[i]);
	}
	for (int i = n - 1; i >= 0; i--) {
		sum += (int)num[i] - 48;
	}
	printf("%d", sum);
	getch();
	return 0;
}
*/
//동적 할당 malloc 이건 남이 푼거 복사한거
#include<stdio.h>
int main() {
	char input[101] = { 0 };
	int n, sum = 0;
	scanf("%d", &n);
	scanf("%s", &input);
	for (int i = 0; i < n; i++) 
		sum += (input[i] - 48);
	printf("%d\n", sum);
	getch();
	return 0;
	}