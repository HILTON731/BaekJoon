#pragma warning(disable:4996)
#define MAX1 10001
#include<stdio.h>
int math_matic(int a) {
	int sum=0;
	int tmp=a;
	while (tmp!=0) {
		sum += (tmp % 10);
		tmp /= 10;
	}
	return (a+sum);
}
int main() {
	int  con[MAX1] = { 0, };
	for (int i = 1; i < MAX1; i++) {
		con[math_matic(i)]=1;
		if (!con[i])
			printf("%d\n", i);
	}
	getch();
	return 0;
}
//15행에서 for(int i = 1;i<MAX1;i++)일땐 
//실행됨
//int i, con[MAX1] = { 0, };
//for (i = 1; i < MAX1; i++)일땐
//실행 X? 왜???
/*
int self_num(int);
int main() {
	int i,j=0,self;

	for (i = 0; i < 10001; i++) {
		self = self_num(i);
		if(j==self){
			j++;
			break;
		}
		else if (j = !self) {
			printf("%d\n", j);
			j++;
		}
	}
	getch();
	return 0;
}
int self_num(int a) {
	int div[5] = { 0, },sum=0;
	div[0] = a % 10;
	div[1] = a / 10000;
	div[2] = (a-div[1])/1000;
	div[3] = (a-div[2])/100;
	div[4] = (a - div[3]) / 10;
	for (int i = 0; i < 5; i++)
		sum += div[i];
	return sum;

}
//wrong

#define MAX 10001
#include <stdio.h>
int Arr[MAX];

int SelfN(int i) {
	int sum = 0;
	int tmp = i;
	while (tmp != 0) {
		sum += (tmp % 10);
		tmp /= 10;
	}
	return (i + sum);
}

int main() {
	for (int i = 1; i <= MAX-1; i++) {
		Arr[SelfN(i)] = 1;
		if (!Arr[i])
			printf("%d\n", i);
	}
	getch();
	return 0;
}//[출처] [c] 백준 4673 셀프 넘버|작성자 Cok
*/
