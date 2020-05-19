#pragma warning(disable:4996)
#include<stdio.h>
void tri_1(int i);
void tri_2(int i);
void blank(int i);
int main() {
	int i, j=3, k, num,count=0;
	scanf("%d", &num);
	while (i > 0) {
		for (i = num - 3; i > 0; i--)
			printf(" ");
		
		i -= 3;
		printf("\n");
	}		
}
void tri_1(){
	printf(' ', ' ', '*', ' ', ' ', "\n");
	printf(' ', '*', ' ', '*', ' ', "\n");
	printf(' *', '*', '*', '*', '*', "\n");
}
void tri_2() {
	printf(' ', ' ', '*', ' ', ' ');
	printf(' ', '*', ' ', '*', ' ');
	printf(' *', '*', '*', '*', '*');
}
// 0-0-7-0-19-13-7-0-25-19-13-7-0
