#include<stdio.h>
int main(){
	/*int i = 0;
	while (i<10){
		printf("1 ");
		i++;
	}*/ //想不执行，用/* */
	int i;
	for (i=1;i<=100;i++){
		//print时候，加；定义变量时候加；
		//printf(类别，变量)用，隔开变量与变量类型，不是；
		printf("%d ",i);
	}
	return 0;
}
