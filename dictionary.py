
字典相当于将索引改为其他的（不止是0,1,2等）

创建字典
dic = {'name':'runoob','likes':123,'urll':'www.runboo.com'}

空字典
dic = {}

修改字典
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

如果有就会更新
tinydict['Age'] = 8 
如果没有就会加入              
tinydict['School'] = "菜鸟教程"  

删除字典某个key
del tinydict['Name']

清空字典
tinydict.clear()

删除字典
del tinydict

字典键的使用：
可以直接利用键来引用字典内容

tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
tinydict['Name']

小菜鸟

键必须不可变
可以用数字、字符串或者元组来充当
但是不可以使用列表


字典内置函数

计算字典元素个数：
len(dic)

输出字典，以字符串形式打印
str(dic)

返回输入的变量类型，这样会返回字典类型
type(dic)

<class 'dict'>

dic.copy()