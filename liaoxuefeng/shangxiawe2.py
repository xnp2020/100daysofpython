from contextlib import contextmanager

class Query:
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()
    #代码执行顺序：先执行yield之前的代码，然后执行with里面的代码，最后执行yield后面的代码


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('world')