def s_dig(n):
    if n // 10 == 0:
        return n % 10
    else:
        return n % 10 + s_dig(n // 10)
print(s_dig(int(input())))



