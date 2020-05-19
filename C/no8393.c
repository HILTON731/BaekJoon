#pragma warning(disable:4996)
#include<stdio.h>
#include<assert.h>
int NUM1, i;
/*static*/ int STORE=0;
int main() {
	assert(1 <= NUM1 <= 10000);
	scanf("%d", &NUM1);
	for (i = 0; i < NUM1; i++) {
		STORE += (NUM1 - i);
	}
	printf("%d", STORE);
	getch();
	return 0;
}
//static 을 이용한 방법은 없을까?