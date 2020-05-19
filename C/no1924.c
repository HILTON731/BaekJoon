#pragma warning(disable:4996)
#include<stdio.h>
int date, month, i, j=0;
char day[7][4] = {"SUN", "MON", "TUE", "WED","THU","FRI","SAT"};
int END_DATE[] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
const int DIV = 7;

int main(){
	scanf("%d %d", &month, &date);
	for (i = 0; i < month;i++) {
		if (i == (month - 1))
			j += date;
		else
			j += END_DATE[i];
	}
	printf("%s", day[j%DIV]);

	getch();
	return 0;
}