# def func(letter):
#     print(letter)
# 1.下面这个函数，分别使用关键字参数，以及默认参数的方式传参
# 2.并说明在函数中有return和没有return的区别。（代码需要格式化）

#关键字参数传参
def func(letter):     #定义一个函数func
    print(letter)     #打印letter的值
    return 1           #函数返回空
print(func(letter=1))    #调用func函数时给letter赋值1

# #默认参数传参
# def func(letter=1):     #定义一个函数func,默认参数letter的值为1
#     print(letter)       #打印letter的值
# print(func())           #调用func函数