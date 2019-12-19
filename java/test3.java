// 定义了一个bubbleSort的方法
public class test3{
	public static void bubbleSort(int array[]){
		int t=0;
		// 数组长度：array.length
		for (int i=0;i<array.length-1;i++)
			for (int j=0;j<array.length-1-i;j++)
				if (array[j]>array[j+1]){
					t=array[j];
					array[j]=array[j+1];
					array[j+1]=t;
				}
	}			
}
