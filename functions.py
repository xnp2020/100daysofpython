# 函数

def power(x, n=2):
    '''按顺序提供默认参数，当不按顺序提供部分默认参数时，需要把参数名写上。'''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def calc(*numbers):
    '''可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。'''
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
calc(*nums)     #Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

def person(name, age, **kw):
    '''关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。'''
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)    #**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
