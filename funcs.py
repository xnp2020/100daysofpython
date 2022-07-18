# map/reduce函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2float(s):
    '''字符串转换成浮点数'''
    while s[-1] == '0':
        s = s[:-1]
    str_index = s.rfind('.')
    division_length = len(s) - str_index - 1 #除以10的division_length次方
    return reduce(lambda x, y: x * 10 + y, map(char2num, s.replace('.','')))/(10**division_length)


from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2int(s):
    '''字符串转整型'''
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# filter函数
'''计算回数'''
def is_palindrome(n):
    n = str(n)
    if len(n) % 2 == 0:
        if n[:] == n[::-1]:
            return n
    else:
        str_index = len(n)//2 + 1
        if n[:str_index] == n[::-1][:str_index]:
            return n

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

filter(is_palindrome, range(1, 1000))


'''计算素数（埃氏筛法）'''
def _odd_iter():
    '''构造一个从3开始的奇数序列'''
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    '''定义筛选函数'''
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break