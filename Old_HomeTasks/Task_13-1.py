def fu13_1():
    x = 1
    while True:
        if x % 2 == 0:
            yield -x
        else:
            yield x
        x += 1
gf = fu13_1()
for _ in range(10):
    print(next(gf), end=',')





