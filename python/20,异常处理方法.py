# 出现异常时候程序执行不下去

a = 100
print(b)
print(a)


# 使用try，except，else，可以在出现异常部分报错，后续部分正常执行
# try：要执行的内容(可能有错误的部分)  except：错误的内容怎么显示  else：正确的内容怎么显示 finally:不管怎么样都执行

a = 100
try:
    print(b)
except Exception as e:
    print(e)
print(a)

# 在强转类型时候

strs = input("请输入一组带空格的数字")
lists = strs.split()   # 将输入的内容转化为列表strs.split("")
new_lists = []
for i in lists:
    try:
        element = int(i)
    except Exception as e:
        print(e)
    else:
        new_lists.append(element)
print(new_lists)

# 自定义异常,抛出异常的结果
strs = input("请输入一组带空格的数字")
list = strs.split()
if len(list) <= 5:
    print(list)
else:
    a = Exception("列表长度大于5")  # Exception(自己定义的显示异常的内容)
    raise a                       # raise用来抛出异常的内容


