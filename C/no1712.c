#pragma warning(disable:4996)
#include<stdio.h>
int account(int a, int b, int c) {
	//int i = 0 , sum1, sum2;
	/*while (b<c) {
		sum1 = a + (b * i);
		sum2 = c * i;
		
		if (sum1 < sum2)return i;
		i++;
	}*/
	if (b < c)return a / (c - b)+1;
	else return -1;
}
int main() {
	int fixed_cost, unfixed_cost, income;
	scanf("%d %d %d", &fixed_cost, &unfixed_cost, &income);

	
	printf("%d", account(fixed_cost, unfixed_cost, income));
	getch();
	return 0;	
}