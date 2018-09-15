# -*- coding: utf-8 -*-

# import size
# x = int(input('num1:'))
# y = int(input('num2:'))
# print(size.jiafa(x,y))



def fun(s):
    try:
        if type(1) == type(int(s)):
            print('是一个数字')
    except ValueError as e:
        print(e,'你输入的不是数字')
    return s

fun(2)