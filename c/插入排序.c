#include <stdio.h>
int main(){
	int a[]={12,4,8,6,5,0,9};
	int n=7;
	int tem=0;
	for (int i=1;i<n;i++){
		printf("%d\n",a[i]);
		int j=i-1;
		if (a[i]<a[j]){
			printf("%d,%d\n",a[i],a[j]);
			tem=a[i];
			a[i]=a[j];
			printf("%d,%d\n",a[i],a[j]);
			while (tem<a[j-1]){
				a[j]=a[j-1];
				j==;
			}
			a[j]=tem;
			printf("%d",a[j]);

		}
	}
}