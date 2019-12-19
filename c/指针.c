#include <stdio.h>

// int main(){
// 	int a = 100;
// 	char b[2] = "dg";
// 	printf("%p\n,%p\n", &a, b);
// }

int main(){
	char c = 'f';
	// *指针说明符；&代表提取地址 
	char *p1 = &c;
	// 打印时候*会报错
	printf("%p", p1);
	printf("%d", (int) p1);
	int a = 1;
	int a = 100;
	printf("%d", a); 

}
int a = 15;
// 指针变量*p  取地址运算符&
int *p=&a; 
// *是一个指针标识符，只说明一次就行了，否则会报错；int 是指后边a变量内容类型

*p1=a;
printf("%d",*p1);
// printf中*p1,*是间址运算符，不是指针标识符了，它的意义是通过指针变量获取数据，格式是：间址运算符 指针变量名（*p)。
*p2=&b;
// 这里边的*是指针标识符
// *可以表示三种意义：乘法；指针标识符；间址运算符（通过指针变量获取数据）
p1=&c;
printf("%d",p1);
p2=&d;
// 通过直接再次赋值，就可以将指针变量改变
 int a =15;
int *p=a;
printf("%d",*p);
int a = 123123;
int *p = &a;
printf("%p\n", p);
p += 1;
printf("%p\n", p);
printf("%d\n", *p);
int arr[3] = {11,22,33};
int *p = &arr[3];
printf("%d\n", *p);
printf("%d\n", *(p+1));
printf("%d\n", *(p+2));
/printf("%d\n", *(p-3));
int *p = (int *)(unsigned long)4330312944;
printf("%d\n", *p);
return 0;
}

 *&a=a &*p=&a=p
*,&相当于乘，除的关系



