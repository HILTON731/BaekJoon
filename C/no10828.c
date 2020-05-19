#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<malloc.h>

#define MAX_STACK_SIZE 10000
typedef struct StackType {
	int data[MAX_STACK_SIZE];
	int stop;
}StackType;
void push(StackType *s, int data) {
	s->data[++s->stop] = data;
}
void pop(StackType *s) {
	if (s->stop == -1) 
		printf("%d\n",s->stop);
	else
		printf("%d\n",s->data[s->stop--]);
}
void size(StackType *s) {
	printf("%d\n", s->stop + 1);
}
void empty(StackType *s) {
	if (s->stop == -1)
		printf("1\n");
	else
		printf("0\n");
}
void top(StackType *s) {
	if (s->stop == -1) printf("-1\n");
	else printf("%d\n",s->data[s->stop]);
}
int main() {
	StackType *s=(StackType*)malloc(sizeof(StackType));
	int command, item;
	char a[7];
	s->stop = -1;
	scanf("%d", &command);
	for (int i = 0; i < command; i++) {
		scanf("%s", a);
		if (!strcmp(a,"push")) {
			scanf("%d", &item);
			push(s, item);
		}
		else if (!strcmp(a, "pop")) {
			pop(s);
		}
		else if (!strcmp(a, "size")) {
			size(s);
		}
		else if (!strcmp(a, "empty")) {
			empty(s);
		}
		else if (!strcmp(a, "top")) {
			top(s);
		}
	
	}
	getch();
	return 0;
}