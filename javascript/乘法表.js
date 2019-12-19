<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset = "UTF-8">
	<title>$ 永远的24k纯帅 $</title>
	<script...>

	<script>
		// js代码
		alert("12345"); // 在页面中弹出对话框  
		                // js代码执行的注意问题：1，在一对script标签中有错误的js代码，则后边的js代码不会执行
		                // 2，如果第一对的script标签中有错误，不会影响下一对的执行
		                // 3,script 的标签中可以写type="text/javascript"是标准写法或者“language="JavaScript”都可以，目前的页面中这两个都可以省略
		                // script标签一般是放在body的标签的最后
		                // 如果script标签中要引用文件，不要写任何代码，再加个新的标签进行
		                // 变量申明用var，每行代码结束都应该有；1，如果名字有多个单词就第一个单词首字母小写之后的所有单词首字母都大写var studentGrade=8; 3，申明var num;4,变量初始化：var num=10;5,申明多个变量var num1,mum2,mum3; num1=10...;或者var num1=10,num2=20,num3=30;6，变量命名注意不能使用关键字，由字母，下划线，数字，符号组成，不能以数字开头
		                // console.log(num); 把内容输出在浏览器的控制台中

	</script>
</head>
<body>


</body>
</html> 

<script>
	/* js分为三个部分：ECMAScript 语法；DOM document object model 文档对象模型；BOM brower 
	* 编译语言是将代码翻译成计算机认知的二进制语言才能执行，脚本语言是不需要编译直接执行的
	* 常见的脚本语言有：t-sql  cmd jacascript是运行在客户端的脚本语言
	* 电脑硬件--系统--客户端的程序（浏览器）---代码
    * 页面中代码：html展示页面的  css美化页面的 js-控制页面的
    * js的代码可以在三个地方写：1，html的文件中，script的标签中写；2，html的标签中写 3，js文件中写，需要在html的文件中引用，script的标签中src=“js的路径”


    * 一个变量交换的思想：1，第三个变量 2，运算方式 3，num1=10;num2=20;  num1=num1^num2 num2=num1^num2 num1=num^num2 位运算
	*/
	var i = 0, sum = 0;
	do{
		if(i%3==0){
			sum += i;
		}
		i++
	}while(i<=10);
	console.log(sum);


	// 九九乘法表
	for (var i=1;i<=9;i++){
		for (var j=1;j<=i;j++){
			var a = i * j;
			console.log(i,"*",j,"=",a)
		}
	}


	// 冒泡排序
	var arr = [3,5,2,4];
	for (var i=0;i<arr.length;i++){
		for (var j=i;j<arr.length;j++){
			if (arr[i]>arr[j]){
				var temp;
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
	console.log(arr)

	// 快速排序
	


</script>
.
.
</body>
</html> 