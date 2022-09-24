import itertools


def pi(N):
    """计算pi的值"""
    # 创造一个奇数序列：1,3,5,7...
    odd = itertools.count(start=1, step=2)
    # 取该奇数序列的前N项
    odd_n = itertools.takewhile(lambda x: x <= 2*N - 1, odd)
    # 添加正负号并用4除
    m = 0
    list_n = []
    for i in odd_n:
        list_n.append(4/(i*(-1)**m))
        m = m+1

    #iter_1 = itertools.cycle([-1,1])
    #for i in odd_n:
    #    list_n.append(4*next(iter_1)/i)

    return sum(list_n)
