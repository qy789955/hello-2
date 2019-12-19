#include <stdio.h>
int main(){
	printf("bfbfbfb11");
	int i,j;
	// 每出现一个新的命令，都用{}包围起来
	for (i=1;i<=9;i++){  
		for (j=1;j<=i;j++){
			// 定义输出内容时候，先定义内容的类型，字符串为%d 
			printf("%d*%d=%d ",i,j,i*j);
		}
		printf("\n");
	}
}
