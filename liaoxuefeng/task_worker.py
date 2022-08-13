from socket import timeout
import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManageer(BaseManager):
    pass

QueueManageer.register('get_task_queue')
QueueManageer.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
m = QueueManageer(address=(server_addr, 50000),authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
print('worker exit')