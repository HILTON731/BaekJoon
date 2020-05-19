#pragma warning (disable:4996)
#include<stdio.h>
#define MAX_QUE_SIZE 10000
typedef struct quenode {
	int data[MAX_QUE_SIZE];
	int front, rear;
}quenode;

void init(quenode *q) {
	q->front = q->rear = 0;
}
int main() {
	printf("hello");
	getch();
	return 0;
}