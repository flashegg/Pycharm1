# -*- coding: utf-8 -*-
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)


# sum = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s * %s = %s" %(j,i,j * i),end="  ")
#     print()


# l1 = [1,2]
# for i in range(6):
#     l1.append(l1[-1] + l1[-2])
# print(l1)

# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)

# import sys
# for i in range(10):
#     if i == 3:
#         continue
#     elif i == 5:
#         pass
#     elif i == 8:
#         sys.exit()
#     print(i)
#
# x = ''
# prompt = """-------------------------
# 1、矿泉水
# 2、可口可乐
# -------------------------
# """
# while not x:
#     print('请选择菜单内容：')
#     x = input((prompt))
#     if x == '1':
#         print('1元')
#     elif x == '2' :
#         print('3元')



# x = ''
# while x != 'q':
#     print('hello')
#     x = input('please input something:')

# sum = 0
# counter = 1
# while counter <= 100:
#     sum = sum + counter
#     counter = counter + 1
# print(sum)

# tc = 0
# username = input('name:')
# password = input('password:')
# while True:
#     if username == 'tom' and password == '123':
#         print('登陆成功')
#         break
#     else:
#         tc = tc + 1
#         print('登录失败%s次' %(tc))
#     username = input('name:')
#     password = input('password:')
#     if tc == 2:
#         print('登录失败3次，退出')
#         break


# f1 = open('/proc/meminfo','r')
# for lines in f1:
#     if lines.startswith('MemTotal:'):
#         memtotal = int(lines.split()[1]) / 1024
#     if lines.startswith('MemFree:'):
#         memfree = int(lines.split()[1]) / 1024
#         break
# print('Used:%.2f - %.2f = %.2f' %(memtotal,memfree,memtotal - memfree))


# def power(x,y):
#     return "%s + %s = %s" %(x,y,x + y)
#
# def power2(x,y):
#     return "%s - %s = %s" %(x,y,x - y)
#
# print(power(5,2))



# def fun(x,y):
#     s = 1
#     while y > 0:
#         y = y - 1
#         s = s * x
#     return s
#
# def fun2(x,y):
#     return x ** y
#
#
# print(fun2(5,3))