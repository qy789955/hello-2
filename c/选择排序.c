#include <stdio.h>
int main(){
	int a[]={12,4,8,6,5,0,9};
	int n=7;
	int i,key=i;
	for (i=0;i<n;i++){
		for (int j=i+1;j<n;j++){
			printf("%d,%d\n",a[i],a[j]);
			if (a[j]>a[i]){
				a[key]=a[i];
				a[i]=a[j];
				a[j]=a[key];
				printf("%d\n",a[i]);
			}
		}
	}
	for (int k=0;k<n;k++){
		printf("%d",a[k]);
	}
	return 0;
}