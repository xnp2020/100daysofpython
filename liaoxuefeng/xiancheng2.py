import time, threading

# 假定这是你的银行存款:
balance = 0
lock1 = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(200000000):
        #获取锁
        lock1.acquire()
        try:
            change_it(n)
        finally:
            #释放锁
            lock1.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)