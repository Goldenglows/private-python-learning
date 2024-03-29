元组的使用（）

tuple

元组的创建：

tup1 = ('goole','runboo',1992,2000)
tup2 = (1,2,3,4,5,6)
tup3 = "a","b","c"          #不用括号也可以这种

创建空元组：
tup = ()

只有一个元素，要加逗号才能创建元组类型
tup = (50,)
tup = (50)    #这样相当于定义了一个int类型

切片：与list类似

tup[1:5]    #值第二个到第五个元素，包括第五个

修改元组
直接相加：
tup3 = tup1 + tup2

del tup #直接删除整个元组

取长度

len((1,2,3))

3

连接
a = (1, 2, 3)
b = (4, 5, 6)
a += b

a        (1,2,3,4,5,6)

复制
('Hi!',) * 4

('Hi!', 'Hi!', 'Hi!', 'Hi!')

判断是否存在
3 in (1,2,3)

True

元组内置函数

返回元组中元素最大值
max(tuple)

返回元组中元素最小值
min(tuple)

将其他的类型转换为元组
tuple(list)

元组指向的内存中的内容不可变

tup = ('r', 'u', 'n', 'o', 'o', 'b')
tup[0] = 'g'     # 不支持修改元素
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

所绑定到了新的对象

>>> id(tup)     # 查看内存地址
4440687904
>>> tup = (1,2,3)
>>> id(tup)
4441088800    # 内存地址不一样了