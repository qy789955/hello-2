import pandas as pd
# 实现and逻辑运算，给它权重，需要将结果显示出来并且判断有没有错误
# 赋值权重和偏差
weight1 = 1.5
weight2 = 1
bias = -1.5

# 获取输入值输出值
test_inputs = [(0,0),(0,1),(1,0),(1,1)]
correct_outputs = [False,False,False,True]
outputs = []

# 进行内部测试
# zip可以返回一个元组，zip参数若只有一个，则从中选出一些元素组成新的元组，若参数有两个，则两个参数中分别对应取值，组成新的元组
for test_input,correct_output in zip(test_inputs,correct_outputs):
    linear_combination = weight1*test_input[0] + weight2*test_input[1] + bias
    output = int(linear_combination >= 0) # int(a>0),a>0时候输出1，否则输出为0
    is_correct = "yes" if output == correct_output else "no"
    # 在输出列表中添入新的元素
    outputs.append([test_input[0],test_input[1],linear_combination,output,is_correct])

# 形成dataframe的表格形式
a = pd.DataFrame(outputs,columns=["Input1","Input2","linear combination","output","is correct"]) # columns参数要是列表的形式
# 去掉索引值
b = a.to_string(index=False)
print(b)

# 计算机告诉有几个错误
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
print("You got {} wrong.".format(num_wrong))
'''
    str.format(),此方法通过字符创中的{}来识别后边的替换字段，从而传参数
        {}内部的字段形式有很多：1，数字字段{1}{0]{2}  代表替换字段的位置，每个位置对应的内容可以多次使用 print('身高{0}，家住{1},妹妹身高也是{0}。'.format(1.8, '铜锣湾'))
        2,省略字段，此时是一一对应的关系 print('身高{}，家住{}。'.format(1.8, '铜锣湾'))
        3,变量名字段，print('身高{length}，家住{home}。'.format(length=1.8, home='铜锣湾'))
        4，混用字段，但是省略字段和数字字段不能混用 print('身高{0}，家住{home}。'.format(1.8, home='铜锣湾'))
        5，元组或者字典字段：
        元组：info='钢铁侠', 66, '小辣椒'  print('我是{}，身价{}亿。'.format(*infos))
        字典：venom = {'name': '毒液', 'weakness': '火'} print('我是{name}，我怕{weakness}。'.format(**venom)) 
        注意元组和字典对应的引号个数不一样
    '''
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))





