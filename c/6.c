#include <stdio.h>
int main(){
	int a,b,min;
	//赋值变量时候加；
	a=3;	
	b=4;
	if(a>b){		
		min=b;
		/*b=a;
		printf("%d",b);
		a=min;
		printf("%d",a);*/
	}
	printf("%d",min);
	return 0;
}