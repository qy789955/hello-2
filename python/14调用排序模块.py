# 1,用import调用模块
import paixu            # import导入模块
list1 = [12,3,5,2,4,8]  # 注意数组之间的数用，隔开
list2 = paixu.mp(list1)   # 用模块调用里边的函数
print(list2)

# 2，从模块直接导入某个函数：form 模块名 import 函数名
from paixu import mp
list1 = [12,3,5,2,4,8]  # 注意数组之间的数用，隔开
list2 = mp(list1)   # 注意由于函数直接被导入了，所以直接传参数使用，不用调用
print(list2)

# 3，从模块直接导入所有函数 form 模块名 import *
from paixu import *
list1 = [12,3,5,2,4,8]  # 注意数组之间的数用，隔开
list2 = mp(list1)   # 注意由于函数直接被导入了，所以直接传参数使用，不用调用
print(list2)

# 4，从模块直接导入某个函数并且新命名为新的名字 form 模块名 import mp as a
from paixu import mp as a
list1 = [12,3,5,2,4,8]  # 注意数组之间的数用，隔开
list2 = a(list1)   # 注意由于函数直接被导入了，所以直接传参数使用，不用调用
print(list2)

