function bubbleSort(arr){
	var len=arr.length;  // var定义变量
	for (var i=0;i<len;i++){  // 直接定义变量var i=0;没有定义变量数据类型
		for (var j=i+1;j<len;j++){
			if (arr[j]>arr[i]){
				var temp=arr[j];
				arr[j]=arr[i];
				arr[i]=temp;
			}
		}
	}
	return arr;
}
	var arr=[3.4.2,6];
	window.bubbleSort(arr);
// 调用函数是用对象调用函数，浏览器中对象是window（浏览器窗口）,js中默认的全局对象是函数，html中默认的全局对象html页面本身，函数属于html页面