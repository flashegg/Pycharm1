
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# a = int(input('请输入一个数：'))
# print(my_abs(a))