from hehe_1 import my_abs

#x的n次方等于n个x相乘，这里的s是累乘的值，就是结果
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# def power(x,n):
#     s = x ** n
#     return s

print(power(5,3))
