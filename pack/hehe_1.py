# -*- coding: utf-8 -*-

def fun(s):
    try:
        if type(1) == type(int(s)):
            print('是一个数字')
    except ValueError as e:
        print(e,'你输入的不是数字')
    return s