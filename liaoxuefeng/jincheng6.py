import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x + 1

for i in range(multiprocessing.cpu_count()):
    p = multiprocessing.Process(target=loop)
    p.start()
    p.join()