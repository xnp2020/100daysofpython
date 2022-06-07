"""
本意是打印pingpong共10个,结果打印的是pingpong各10个，因为每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量。
解决办法是使用multiprocessing模块中的Queue类，它是可以被多个进程共享的队列，底层是通过管道和信号量（semaphore）机制来实现的。
"""


from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()
