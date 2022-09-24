def mul(x, *y):
    if len(y) == 0:
        return x
    else:
        s = x
        for num in y:
            s = s * num
        return s