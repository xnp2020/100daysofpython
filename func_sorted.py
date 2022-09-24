def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call')
        return func(*args,**kw)
    return wrapper
    
#带参数的装饰器
def log(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
            return func(*args,**kw)
        return wrapper
    print('end call')
    return decorator

def log(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


class Student(object):
    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height    
    @property
    def resolution(self):
        return self._width * self._height

class St():
    pass
    def __str__(self) -> str:
        return 'instance'
    __repr__ = __str__
    

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10/n
