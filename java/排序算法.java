// 定义了一个bubbleSort的方法
public class test4{
 	public static int[] bubbleSort(int[] array1){
 		// 最好先用其他数组接收一下这个数组，这样就不会在原数组的基础上改动
 		int array[] = array1.clone();
 		if (array.length==0)
 			return array;
		// 数组长度：array.length
		for (int i=0;i<array.length;i++){
			for (int j=0;j<array.length-1-i;j++){
		 		if (array[j]>array[j+1]){
		 			int t=array[j];
					array[j]=array[j+1];
		 			array[j+1]=t;
		 		}
	 		}
 		}
		return array;
 	}
 	// 调用这个方法时候必须类型与int一致，比如array2【k】，所代表的每一个元素都是int
 	public static void pt(int str){
 		System.out.println(str);
 	}
 	// int和int[]不同，int代表绝对整型，int【】是指数组位置的类型
 	public static void ptarr(int[] str){
 		System.out.println(str);
 	}
 	public static void main(String[] args){
		// 传参数
		int a[]={11,2,3,4,5};
		// 调用方法bubbleSort(a);新的结果用新的数组接收
		int array2[] = bubbleSort(a);
		ptarr(array2);
		for (int k=0;k<array2.length;k++){
			pt(array2[k]);
		}
		// 可以在运行主体中加一个return，保证系统不会有异常执行不到return的报错
	}
}