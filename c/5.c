#include <stdio.h>
int main(){
	//定义数组：类型（int，float，char+数组名字+【元素个数】={元素1，元素2，。。。}
	int a[6]={3,5,6,2,8,1};
	//使用变量前先定义变量类型
	int i,j;
	//for 循环内容要加分号隔开内容，for后不用；
	for(j=0;j<=4;j++){
		//printf，每一步循环，printf一个数字，可以看出计算机到底怎么循环的
		for(i=j+1;i<=5;i++){
			if(a[j]>a[i]){
				int temp = a[j];
				a[j] = a[i];
				a[i] = temp;							
			}
		}		
	}
	//最后一个循环结束，输出的是最后一个结果
	printf("%d", a[j]);

	int k;
	for(k = 0; k <= 5; k++){
		printf(",");
		printf("%d", a[k]);
	}
	printf("\n");
	//printf用，隔开
	//记得用return 0；来结束函数
}