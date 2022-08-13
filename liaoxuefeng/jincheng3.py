from multiprocessing import Pool
import os,time,random

# 子进程要执行的代码
def run_proc(name):
    print('start run child process %s(pid %s)' % (name,os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 3)
    end_time = time.time()
    print('child process %s(pid %s) spent %.2f secs' % (name,os.getpid(),end_time-start_time))

if  __name__=='__main__':
    print('Parent process id is %s' % os.getpid())
    p = Pool() #Pool默认参数为cpu个数
    for i in range(13):
        p.apply_async(run_proc, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join() #等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    print('All Child process done.')