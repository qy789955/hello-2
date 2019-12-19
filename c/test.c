#include <stdio.h>

int main(){
	printf("1. 程序开始运行：");
	int arr[] = {-8,0,11,8,44,6,85,58223,9,8,92, 53};
	int len1 = sizeof(arr);
	int len2 = sizeof(int);
	int len = len1 / len2;
	printf("\n2. 这个数组总共占用比特数:");
	printf("%d", len1);
	printf("\n3. 这个数组中每个元素int的占用比特:");
	printf("%d", len2);
	printf("\n4. 这个数组的元素个数是:");
	printf("%d", len);

	printf("\n5. 查看这个数组中所有的元素：");
	int i;
	for(i = 0; i < len; i++){
		printf(",");
		printf("%d", arr[i]);
	}

	printf("\n6. 开始排序，从小到大");
	int j, k;
	for(j = 0; j < len; j++){
		int a = arr[j];
		for(k = j+1; k < len; k++){
			int b = arr[k];
			// printf("\na:");
			// printf("%d", a);
			// printf(",b:");
			// printf("%d", b);
			if(a > b){
				// printf("(True)");
				int c = arr[j];
				arr[j] = arr[k];
				arr[k] = c;
			}
		}
	}

	printf("\n7.排序，完成，查看结果：");
	int q;
	for(q = 0; q < len; q++){
		printf(",");
		printf("%d", arr[q]);
	}

	printf("\n");
	
}
