import time
import threading

'''主线程之外开启1个额外的线程'''

def loop():
    print('thread %s is running.' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print("I'm 主线程，线程名： %s" % threading.current_thread().name)
t = threading.Thread(target=loop, name='线程1') #name如果不指定，则默认为Thread-1，Thread-2...
t.start()
t.join()
print('主进程 %s 结束了。' % threading.current_thread().name)
