#include <stdio.h>
int main(){
	// int a =100;
	// int *p;
	// p=&a;
	// int *p=100 // 此时为间指运算符
	int a = 10,*pa=&a,*paa=&a;
	// 指针变量的类型是&后变量的类型，有多种
	double b = 99.9,*pb=&b;
	char c = '#',*pc=&c;
	// 内存中地址都是整型，&a对应的为整型数字
	printf("%d,%d,%d\n",&a,&b,&c);
	printf("%d,%d,%d\n",pa,pb,pc);
	// 加法运算
	// 加法运算加1不是简单的加1，是加一段；pa++，a为int，加了四个字节；pb++，b为浮点占8字节，所以加了8字节，才能跳到下一个内存；pc++，字符串加1个字节，跳到下一个内存
	pa++;pb++;pc++;
	printf("%d,%d,%d\n",pa,pb,pc);
	pa-=2;pb-=2;pc-=2;
	printf("%d,%d,%d\n",pa,pb,pc);

	// 如果在指针指示位没有内容，此时计算机会随机给出数值，没有意义
	int a=1,b=2,c=3;
	int *p=&c;
	printf("%d\n",*p);
	for (i=1;i<10;i++){
		printf("%d\n",*(p+i));
	}
	// 指针变量可以比较运算
	if (pa==paa){
		printf("%d",pa);
	}
	else{
		printf("%d",paa);
	}
	return 0;
}
