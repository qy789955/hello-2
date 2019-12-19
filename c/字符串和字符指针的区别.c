#include <stdio.h>
int main(){
	// 如果定义了指针数组，此时是不能修改的，会报错bus error
	char *p="bcde"; // 字符指针定义后存在于常量区，只能读，不能写入
	*(p+1)='m';
	// 定义的是正常字符串数组，可以修改
	char a[]="bcde";  //  字符数组存在于全局区或者栈区，既可以读也可以写
	a[1]='a';
	printf("%s",a);
	return 0;
}