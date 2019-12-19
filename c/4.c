/*#include <stdio.h>
int main(){
	/*int x,y,max;
	//让输入数据，格式是scanf(“规定类型”，&变量)；与输出类似
	scanf("%d%d",&x,&y);
	if (x<y) max=y;
	else max=x;
	printf("%d",max);
	return 0;
}*/
#include <stdio.h>
int main(){
	//定义数组：类型（int，float，char+数组名字+【元素个数】={元素1，元素2，。。。}
	int a[6]={3,5,6,2,8,1};
	//使用变量前先定义变量类型
	int i,j;
	//for 循环要加分号隔开内容
	for (j=0;j<=4;j++);{
		for (i=j+1;i<=5;i++);{
			if (a[j]>a[i]);
				a[j]=a[i];
		}
	}
	//printf用，隔开
	printf("%d",a);
	//记得用return 0；来结束函数
	return 0;
}
