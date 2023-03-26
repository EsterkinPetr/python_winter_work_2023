def pal():
    i = 1
    while True:
        if str(i) == str(i)[::-1]:
            yield i
            i += 1
        else:
            i += 1
gpal = pal()
for n in range(int(input())):
    print(next(gpal), end=' ')
